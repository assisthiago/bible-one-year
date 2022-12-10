from django import forms
from django.contrib.auth.models import User


class SignInForm(forms.Form):
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput())

    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['email'].widget.attrs['placeholder'] = 'Entre com o seu e-mail'
        self.fields['password'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password'].widget.attrs['placeholder'] = 'Entre com sua senha'


class SignUpForm(SignInForm):
    password_confirmation = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if password and password_confirmation:
            if password != password_confirmation:
                raise forms.ValidationError('Senhas diferentes')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password_confirmation'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password_confirmation'].widget.attrs['placeholder'] = 'Confirme sua senha'
