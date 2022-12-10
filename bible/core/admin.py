from django.contrib import admin

from bible.core.models import Book, Versicle


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Versicle)
class VersicleModelAdmin(admin.ModelAdmin):
    pass
