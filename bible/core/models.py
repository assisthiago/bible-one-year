from django.db import models


class Book(models.Model):
    name = models.CharField('nome', max_length=150)
    abbreviation = models.CharField('abreviação', max_length=3)

    class Meta:
        verbose_name = 'livro'
        verbose_name_plural = 'livros'

    def __str__(self):
        return self.name.capitalize()


class Versicle(models.Model):
    chapter = models.IntegerField('capítulo')
    number = models.IntegerField('versículo')
    text = models.TextField('texto', max_length=255)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name='livro')

    class Meta:
        verbose_name = 'versículo'
        verbose_name_plural = 'versículos'

    def __str__(self):
        return f'{self.chapter}. {self.number}. {self.text}'
