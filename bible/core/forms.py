from django import forms
from django.contrib.auth.models import User


class SignInForm(forms.Form):
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput())

    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['email'].widget.attrs['placeholder'] = 'Entre com o seu e-mail'
        self.fields['password'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password'].widget.attrs['placeholder'] = 'Entre com sua senha'
