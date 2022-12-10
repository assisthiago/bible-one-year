from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r

from bible.core.forms import SignInForm


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)

        if not form.is_valid():
            return render(request, 'sign_in.html', {'form': form})

        user = authenticate(
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password'])

        if not user:
            messages.error(request, 'E-mail ou senha incorreta')
            return render(request, 'sign_in.html', {'form': form})

        return HttpResponseRedirect(r('home'))

    return render(request, 'sign_in.html', {'form': SignInForm()})


def home(request):
    return render(request, 'index.html')
