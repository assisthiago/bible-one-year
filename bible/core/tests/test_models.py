from django.contrib.auth.models import User
from django.test import TestCase

from bible.core.models import Book, Versicle


class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='thiago@assis.com',
            password='1234567890',
            email='thiago@assis.com')

    def test_user(self):
        self.assertTrue(User.objects.exists())

    def test_username(self):
        self.assertEqual('thiago@assis.com', self.user.username)

    def test_email(self):
        self.assertEqual('thiago@assis.com', self.user.email)

    def test_password(self):
        self.assertEqual('1234567890', self.user.password)


class BookTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(name='gênesis', abbreviation='gn')

    def test_book(self):
        self.assertTrue(Book.objects.exists())

    def test_name(self):
        self.assertEqual('Gênesis', str(self.book))


class VersicleTest(TestCase):
    def setUp(self):
        book = Book.objects.create(name='gênesis', abbreviation='gn')

        self.versicle = Versicle.objects.create(
            chapter=1,
            number=1,
            text='No princípio, Deus criou os céus e a terra.',
            book=book)

    def test_book(self):
        self.assertTrue(Versicle.objects.exists())

    def test_name(self):
        self.assertEqual(
            '1. 1. No princípio, Deus criou os céus e a terra.',
            str(self.versicle))
