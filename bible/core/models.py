from django.contrib.auth.models import User
from django.db import models

from bible.core.managers import BookTestamentQuerySet


class Lection(models.Model):
    order = models.IntegerField('ordem')

    class Meta:
        verbose_name = 'leitura'
        verbose_name_plural = 'leituras'
        ordering = ('order',)

    def __str__(self):
        return f'{self.order}a. Leitura'


class Book(models.Model):
    NEW_TESTAMENT = 'new'
    OLD_TESTAMENT = 'old'
    TESTAMENT_CHOICES = (
        (OLD_TESTAMENT, 'antigo'),
        (NEW_TESTAMENT, 'novo'),
    )

    name = models.CharField('livro', max_length=150)
    abbreviation = models.CharField('abreviação', max_length=4)
    testament = models.CharField('testemunho', max_length=3, choices=TESTAMENT_CHOICES)
    order = models.IntegerField('ordem', blank=True, null=True, default=None)

    objects = BookTestamentQuerySet.as_manager()

    class Meta:
        verbose_name = 'livro'
        verbose_name_plural = 'livros'
        ordering = ('testament', 'order')

    def __str__(self):
        return self.name.title()


class Versicle(models.Model):
    chapter = models.IntegerField('capítulo')
    number = models.IntegerField('número')
    text = models.TextField('texto', max_length=350)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name='livro')
    lection = models.ForeignKey('Lection', on_delete=models.CASCADE, blank=True, null=True, verbose_name='leitura')


    class Meta:
        verbose_name = 'versículo'
        verbose_name_plural = 'versículos'
        ordering = ('book__testament', 'book__name', 'chapter', 'number')

    def __str__(self):
        return f'{self.book.abbreviation} {self.chapter},{self.number}'.title()


class Task(models.Model):
    completed = models.BooleanField('concluído', default=False)
    completed_at = models.DateField('completado em', default=None, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name='usuário', db_index=True)
    lection = models.ForeignKey('Lection', on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name='leitura', db_index=True)

    class Meta:
        verbose_name = 'tarefa'
        verbose_name_plural = 'tarefas'

    def __str__(self):
        return f'Tarefa: {self.lection}'
