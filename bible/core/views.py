from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r

from bible.core.forms import SignInForm, SignUpForm


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


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if not form.is_valid():
            return render(request, 'sign_up.html', {'form': form})

        try:
            User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'])

        except:
            messages.error(request, 'Usuário existente')
            return render(request, 'sign_up.html', {'form': form})


        messages.success(request, 'Conta criada com sucesso')
        return HttpResponseRedirect(r('sign-in'))

    return render(request, 'sign_up.html', {'form': SignUpForm()})


def home(request):
    return render(request, 'index.html')
