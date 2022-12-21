from django.db import models


class Lection(models.Model):
    order = models.IntegerField()
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'leitura'
        verbose_name_plural = 'leituras'
        ordering = ('order',)

    def __str__(self):
        return f'Dia {self.pk}'


class Versicle(models.Model):
    book = models.CharField('livro', max_length=150)
    book_abbreviation = models.CharField('abreviação', max_length=3)
    chapter = models.CharField('capítulo', max_length=3)
    number = models.CharField('versículo', max_length=3)
    text = models.TextField('texto', max_length=255)
    lection = models.ForeignKey(
        'Lection', on_delete=models.CASCADE, null=True, blank=True, verbose_name='leitura')

    class Meta:
        verbose_name = 'versículo'
        verbose_name_plural = 'versículos'

    def __str__(self):
        return f'{self.book_abbreviation} {self.chapter}:{self.number}'
