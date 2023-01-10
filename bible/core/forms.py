from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from bible.core.models import Book, Lection, Versicle


class SignInForm(forms.Form):
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(),
        validators=[validate_password])

    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['email'].widget.attrs['placeholder'] = 'Entre com o seu e-mail'
        self.fields['email'].widget.attrs['autofocus'] = True
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
                raise forms.ValidationError('Senha informada é diferente da anterior.')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password_confirmation'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password_confirmation'].widget.attrs['placeholder'] = 'Confirme sua senha'


class IncludeVersiclesForm(forms.Form):
    # LECTIONS = Lection.objects.values_list('order', 'order')
    # BOOKS = Book.objects.values_list('pk', 'name')

    LECTIONS = [(order, order) for order in range(1, 333)]
    BOOKS = []

    lection = forms.ChoiceField(
        label='Leitura', choices=LECTIONS)

    book = forms.ChoiceField(
        label='Livros', choices=BOOKS)

    chapters = forms.CharField(label='Capítulos', help_text='Ex.: 1-100')
