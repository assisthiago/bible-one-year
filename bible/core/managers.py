from django.db import models


class BookTestamentQuerySet(models.QuerySet):
    def old_testament(self):
        return self.filter(testament='old')

    def new_testament(self):
        return self.filter(testament='new')
