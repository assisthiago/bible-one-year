from django.contrib import admin

from bible.core.models import Versicle


@admin.register(Versicle)
class VersicleModelAdmin(admin.ModelAdmin):
    list_display = ['versicle', 'book', 'book_abbreviation', 'chapter', 'number']

    def versicle(selg, obj):
        return str(obj)
