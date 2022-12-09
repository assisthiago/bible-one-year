from django.shortcuts import render


def sign_in(request):
    return render(request, 'sign_in.html')


def signup(request):
    return render(request, 'sign-up.html')


def reset_password(request):
    return render(request, 'reset-password.html')


def index(request):
    return render(request, 'index.html')


def versicles(request):
    return render(request, 'versicles.html')
