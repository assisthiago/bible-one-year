from django.shortcuts import resolve_url as r
from django.test import TestCase

from bible.core.forms import SignInForm


class SignInFormTest(TestCase):
    def setUp(self):
        self.form = SignInForm()

    def test_fields(self):
        expected = ['email', 'password']

        self.assertSequenceEqual(expected, list(self.form.fields))
