from django.test import TestCase
from django.shortcuts import resolve_url as r


class SignInTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('sign-in'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'sign_in.html')

    def test_html(self):
        contents = (
            '<form action="/sign-in" method="post">',
            'type="email" name="email"',
            'type="password" name="password"',
            '<button type="submit"',)

        for expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_reset_password_link(self):
        self.assertContains(self.resp, 'href="/reset-password"')

    def test_sign_up_link(self):
        self.assertContains(self.resp, 'href="/sign-up"')
