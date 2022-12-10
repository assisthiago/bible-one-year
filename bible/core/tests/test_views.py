from unittest import SkipTest

from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase

from bible.core.forms import SignInForm, SignUpForm


class SignInGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('sign-in'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'sign_in.html')

    def test_html(self):
        contents = (
            ('type="email" name="email"', 1),
            ('type="password" name="password"', 1),
            ('<button type="submit"', 1),)

        for text, count in contents:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SignInForm)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_reset_password_link(self):
        self.assertContains(self.resp, 'href="/reset-password/"')

    def test_sign_up_link(self):
        self.assertContains(self.resp, 'href="/sign-up/"')


class SignInPostValidTest(TestCase):
    def test_post(self):
        """Valid POST should redirect to /home/"""
        User.objects.create_user(
            'thiago@assis.com',
            'thiago@assis.com',
            'flamengo1')

        data = {'email': 'thiago@assis.com', 'password': 'flamengo1'}
        resp = self.client.post(r('sign-in'), data)

        self.assertRedirects(resp, r('home'))


class SignInPostInvalidTest(TestCase):
    def test_post(self):
        """Invalid POST should show an error message"""
        data = {'email': 'invalid@user.com', 'password': 'flamengo1'}
        resp = self.client.post(r('sign-in'), data)
        self.assertContains(resp, 'E-mail ou senha incorreta.')

    def test_email_errors(self):
        """Invalid email should return an error"""
        data = {'email': 'invalid@email', 'password': '1234567890'}
        resp = self.client.post(r('sign-in'), data)
        self.assertContains(resp, 'Informe um endereço de email válido.')


class SignUpGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('sign-up'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'sign_up.html')

    def test_html(self):
        contents = (
            ('type="email" name="email"', 1),
            ('type="password" name="password"', 1),
            ('type="password" name="password_confirmation"', 1),
            ('<button type="submit"', 1),)

        for text, count in contents:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SignUpForm)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_sign_in_link(self):
        self.assertContains(self.resp, 'href="/sign-in/"')


class SignUpPostValidTest(TestCase):
    def setUp(self):
        self.data = {
            'email': 'thiago@assis.com',
            'password': 'flamengo1',
            'password_confirmation': 'flamengo1'
        }

    def test_post(self):
        """Valid POST should redirect to /sign-in/"""
        resp = self.client.post(r('sign-up'), self.data)
        self.assertRedirects(resp, r('sign-in'))

    def test_message(self):
        """Valid POST should show a success message"""
        resp = self.client.post(r('sign-up'), self.data, follow=True)
        self.assertContains(resp, 'Conta criada com sucesso.')


class SignUpPostInvalidTest(TestCase):
    def setUp(self):
        self.data = dict(
            email='thiago@assis.com',
            password='flamengo1',
            password_confirmation='flamengo1')

    def test_email_errors(self):
        """Invalid email should return an error"""
        data = dict(self.data, email='invalid@email')

        resp = self.client.post(r('sign-up'), data)
        self.assertContains(resp, 'Informe um endereço de email válido.')

    def test_password_confirmantion_errors(self):
        """Invalid password_confirmantion should return an error"""
        data = dict(self.data, password_confirmation='0987654321')

        resp = self.client.post(r('sign-up'), data)
        self.assertContains(resp, 'Senha informada é diferente da anterior.')

    def test_duplicate(self):
        User.objects.create_user(
            self.data['email'],
            self.data['email'],
            self.data['password'])

        resp = self.client.post(r('sign-up'), self.data)
        self.assertContains(resp, 'Usuário já existe.')


class SignOutGetTest(TestCase):
    def test_get(self):
        User.objects.create_user(
                'thiago@assis.com',
                'thiago@assis.com',
                'flamengo1')

        data = {'email': 'thiago@assis.com', 'password': 'flamengo1'}
        self.client.post(r('sign-in'), data)

        resp = self.client.post(r('sign-out'))
        self.assertRedirects(resp, r('sign-in'))


class ResetPasswordGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('reset-password'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'reset-password.html')

    def test_html(self):
        contents = (
            ('type="email" name="email"', 1),
            ('type="password" name="password"', 1),
            ('type="password" name="password_confirmation"', 1),
            ('<button type="submit"', 1),)

        for text, count in contents:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SignUpForm)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_sign_in_link(self):
        self.assertContains(self.resp, 'href="/sign-in/"')


class ResetPasswordPostValidTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'thiago@assis.com',
            'thiago@assis.com',
            'flamengo1')

        self.data = {
            'email': 'thiago@assis.com',
            'password': '1flamengo',
            'password_confirmation': '1flamengo'
        }

    def test_post(self):
        resp = self.client.post(r('reset-password'), self.data)
        """Valid POST should redirect to /sign-in/"""
        self.assertRedirects(resp, r('sign-in'))

    def test_new_password(self):
        self.client.post(r('reset-password'), self.data)
        user = User.objects.get(email=self.user.email)
        self.assertNotEqual(self.user.password, user.password)

    def test_message(self):
        """Valid POST should show a success message"""
        resp = self.client.post(r('reset-password'), self.data, follow=True)
        self.assertContains(resp, 'Senha atualizada com sucesso.')


class ResetPasswordPostInvalidTest(TestCase):
    def setUp(self):
        self.data = dict(
            email='thiago@assis.com',
            password='flamengo1',
            password_confirmation='flamengo1')

    def test_email_errors(self):
        """Invalid email should return an error"""
        data = dict(self.data, email='invalid@email')

        resp = self.client.post(r('reset-password'), data)
        self.assertContains(resp, 'Informe um endereço de email válido.')

    def test_password_confirmantion_errors(self):
        """Invalid password_confirmantion should return an error"""
        data = dict(self.data, password_confirmation='0987654321')

        resp = self.client.post(r('reset-password'), data)
        self.assertContains(resp, 'Senha informada é diferente da anterior.')

    def test_user_not_found(self):
        resp = self.client.post(r('reset-password'), self.data)
        self.assertContains(resp, 'Usuário não encontrado.')


class HomeGetTest(TestCase):
    def test_not_logged_in(self):
        resp = self.client.get(r('home'))
        self.assertRedirects(resp, f'{r("sign-in")}?next={r("home")}')

    def test_get(self):
        pass
