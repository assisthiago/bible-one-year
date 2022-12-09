from django.contrib.auth.models import User
from django.test import TestCase


class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='thiago-assis',
            password='1234567890',
            email='thiago@assis.com')

    def test_user(self):
        self.assertTrue(User.objects.exists())

    def test_username(self):
        self.assertEqual('thiago-assis', self.user.username)

    def test_email(self):
        self.assertEqual('thiago@assis.com', self.user.email)

    def test_password(self):
        self.assertEqual('1234567890', self.user.password)
