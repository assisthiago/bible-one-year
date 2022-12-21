from django.contrib import admin

from bible.core.actions import include_versicles
from bible.core.models import Versicle, Lection


class VersicleInlineModel(admin.TabularInline):
    model = Versicle
    extra = 1


@admin.register(Versicle)
class VersicleModelAdmin(admin.ModelAdmin):
    actions = [include_versicles]
    list_display = ['versicle', 'book', 'book_abbreviation', 'chapter', 'number']
    list_filter = ['book']

    def versicle(self, obj):
        return str(obj)

    versicle.short_description = 'passagem'


@admin.register(Lection)
class LectionModelAdmin(admin.ModelAdmin):
    inlines = [VersicleInlineModel]

    list_display = ['order', 'completed']
