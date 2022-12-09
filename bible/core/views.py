from django.shortcuts import render, redirect, resolve_url as r

from bible.core.forms import SignInForm


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)

        if not form.is_valid():
            return render(request, 'sign_in.html', {'form': form})

        # Validate if email exists
        # Validate if the password is ok

        return redirect(r('home'))

    return render(request, 'sign_in.html', {'form': SignInForm()})


def home(request):
    return render(request, 'index.html')
