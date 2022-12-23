from django.contrib.auth.models import User
from django.db import models


class Lection(models.Model):
    order = models.IntegerField('ordem')

    class Meta:
        verbose_name = 'leitura'
        verbose_name_plural = 'leituras'
        ordering = ('order',)

    def __str__(self):
        return f'dia {self.order}'


class Versicle(models.Model):
    book = models.CharField('livro', max_length=150)
    book_abbreviation = models.CharField('abreviação', max_length=3)
    chapter = models.CharField('capítulo', max_length=3)
    number = models.CharField('versículo', max_length=3)
    text = models.TextField('texto', max_length=255)
    lection = models.ForeignKey('Lection', on_delete=models.CASCADE, null=True, blank=True, verbose_name='leitura', db_index=True)

    class Meta:
        verbose_name = 'versículo'
        verbose_name_plural = 'versículos'
        ordering = ('book', 'chapter')

    def __str__(self):
        return f'{self.book_abbreviation} {self.chapter}:{self.number}'.title()


class Task(models.Model):
    completed = models.BooleanField('concluído', default=False)
    completed_at = models.TimeField('concluído em', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='usuário', db_index=True)
    lection = models.ForeignKey('Lection', on_delete=models.CASCADE, verbose_name='leitura', db_index=True)

    class Meta:
        verbose_name = 'tarefa'
        verbose_name_plural = 'tarefas'

    def __str__(self):
        return f'tarefa: {self.lection}'
