from django.contrib.auth.models import User
from django.db import models


class Lection(models.Model):
    pass
#     order = models.IntegerField('ordem')

#     class Meta:
#         verbose_name = 'leitura'
#         verbose_name_plural = 'leituras'
#         ordering = ('order',)

#     def __str__(self):
#         return f'dia {self.order}'


class Book(models.Model):
    NEW_TESTAMENT = 'new'
    OLD_TESTAMENT = 'old'
    TESTAMENT_CHOICES = (
        (OLD_TESTAMENT, 'antigo'),
        (NEW_TESTAMENT, 'novo'),
    )

    name = models.CharField('livro', max_length=150)
    abbreviation = models.CharField('abreviação', max_length=3)
    testament = models.CharField('testemunho', max_length=3, choices=TESTAMENT_CHOICES)

    class Meta:
        verbose_name = 'livro'
        verbose_name_plural = 'livros'
        ordering = ('testament', 'name')

    def __str__(self):
        return self.name.title()


class Versicle(models.Model):
    chapter = models.IntegerField('capítulo')
    number = models.IntegerField('número')
    text = models.TextField('texto', max_length=255)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name='livro')

    class Meta:
        verbose_name = 'versículo'
        verbose_name_plural = 'versículos'
        ordering = ('book__testament', 'book__name', 'chapter', 'number')

    def __str__(self):
        return f'{self.book.abbreviation} {self.chapter}:{self.number}'.title()


class Task(models.Model):
    pass
#     completed = models.BooleanField('concluído', default=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='usuário', db_index=True)
#     lection = models.ForeignKey('Lection', on_delete=models.CASCADE, verbose_name='leitura', db_index=True)

#     class Meta:
#         verbose_name = 'tarefa'
#         verbose_name_plural = 'tarefas'

#     def __str__(self):
#         return f'tarefa: {self.lection}'
