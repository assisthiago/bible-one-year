# Generated by Django 4.1.3 on 2023-01-10 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('testament', 'order'), 'verbose_name': 'livro', 'verbose_name_plural': 'livros'},
        ),
    ]