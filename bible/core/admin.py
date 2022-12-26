from django.contrib import admin

from bible.core.actions import include_versicles
from bible.core.models import Book, Versicle, Lection, Task


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation', 'testament']
    list_filter = ['testament', 'name']


# class VersicleInlineModel(admin.TabularInline):
#     model = Versicle
#     extra = 1


# @admin.register(Task)
# class TaskModelAdmin(admin.ModelAdmin):
#     pass


@admin.register(Versicle)
class VersicleModelAdmin(admin.ModelAdmin):
    actions = [include_versicles]
    list_display = ['versicle', 'book', 'chapter', 'number']
    list_filter = ['book__testament', 'book']

    search_fields = ('book__abbreviation__exact', 'chapter__exact', 'number__exact')
    search_help_text = 'Formato da busca: 1jo 1 1.'

    def versicle(self, obj):
        return str(obj)

    versicle.short_description = 'versículo'


# @admin.register(Lection)
# class LectionModelAdmin(admin.ModelAdmin):
#     inlines = [VersicleInlineModel]

#     list_display = ['lection', 'order', 'versicles']
#     search_fields = ('order__exact',)
#     search_help_text = 'Buscar apenas pela ordem da leitura.'

#     def lection(self, obj):
#         return str(obj)

#     lection.short_description = 'leitura'

#     def versicles(self, obj):
#         if versicles := obj.versicle_set.all():
#             first_versicle = versicles.first()
#             last_versicle = versicles[len(versicles) - 1]  # Check .last() methods

#             first_book = first_versicle.book_abbreviation
#             last_book = last_versicle.book_abbreviation

#             first_chapter = first_versicle.chapter
#             last_chapter = last_versicle.chapter

#             first_number = first_versicle.number
#             last_number = last_versicle.number

#             return f'{first_book} {first_chapter}:{first_number} - {last_book} {last_chapter}:{last_number}'

#         return 'N/A'

#     versicles.short_description = 'versículos'
