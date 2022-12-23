from django.contrib.auth.models import User
from django.test import TestCase

from bible.core.models import Versicle, Lection, Task


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


class VersicleTest(TestCase):
    def setUp(self):
        lection = Lection.objects.create(order=1)
        self.versicle = Versicle.objects.create(
            book='gênesis',
            book_abbreviation='gn',
            chapter=1,
            number=1,
            text='No princípio, Deus criou os céus e a terra.',
            lection=lection)

    def test_versicle(self):
        self.assertTrue(Versicle.objects.exists())

    def test_name(self):
        self.assertEqual('gn 1:1', str(self.versicle))


class LectionTest(TestCase):
    def setUp(self):
        self.lection = Lection.objects.create(order=1)

    def test_lection(self):
        self.assertTrue(Lection.objects.exists())

    def test_name(self):
        self.assertEqual('dia 1', str(self.lection))


class TaskTest(TestCase):
    def setUp(self):
        lection = Lection.objects.create(order=1)

        Versicle.objects.create(
            book='gênesis',
            book_abbreviation='gn',
            chapter=1,
            number=1,
            text='No princípio, Deus criou os céus e a terra.',
            lection=lection)

        user = User.objects.create(
            username='thiago@assis.com',
            password='1234567890',
            email='thiago@assis.com')

        self.task = Task.objects.create(user=user, lection=lection)

    def test_tak(self):
        self.assertTrue(Task.objects.exists())

    def test_name(self):
        self.assertEqual('tarefa: dia 1', str(self.task))
