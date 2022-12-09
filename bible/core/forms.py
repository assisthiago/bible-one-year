from django import forms
from django.contrib.auth.models import User


class SignInForm(forms.Form):
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput())

    class Meta:
        model = User
