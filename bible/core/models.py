from django.db import models


class Versicle(models.Model):
    book = models.CharField('livro', max_length=150)
    book_abbreviation = models.CharField('abreviação do livro', max_length=3)
    chapter = models.CharField('capítulo', max_length=3)
    number = models.CharField('versículo', max_length=3)
    text = models.TextField('texto', max_length=255)

    class Meta:
        verbose_name = 'versículo'
        verbose_name_plural = 'versículos'

    def __str__(self):
        return f'{self.book_abbreviation.title()} {self.chapter}:{self.number}'
