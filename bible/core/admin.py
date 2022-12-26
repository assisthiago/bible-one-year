from django.contrib import admin

from bible.core.actions import include_versicles
from bible.core.models import Book, Versicle, Lection, Task


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation', 'testament']
    list_filter = ['testament', 'name']


class VersicleInlineModel(admin.TabularInline):
    model = Versicle
    extra = 1

    readonly_fields = ('book', 'chapter', 'number', 'text')


@admin.register(Versicle)
class VersicleModelAdmin(admin.ModelAdmin):
    actions = [include_versicles]
    list_display = ['versicle', 'book', 'chapter', 'number']
    list_filter = ['book__testament', 'book']
    list_per_page = 1000

    search_fields = ('book__abbreviation', 'chapter')
    search_help_text = 'Formato da busca: 1jo 1.'

    def versicle(self, obj):
        return str(obj)

    versicle.short_description = 'versículo'


@admin.register(Lection)
class LectionModelAdmin(admin.ModelAdmin):
    inlines = [VersicleInlineModel]

    list_display = ['lection', 'books', 'chapters', 'order']
    search_fields = ('order__exact',)
    search_help_text = 'Buscar apenas pela ordem da leitura.'
    list_per_page = 20

    def lection(self, obj):
        return str(obj)

    lection.short_description = 'leitura'

    def books(self, obj):
        versicles = obj.versicle_set.all()
        if versicles:
            books = set(str(versicle.book) for versicle in versicles)
            return ', '.join(sorted(books))

        return 'N/A'

    books.short_description = 'livros'

    def chapters(self, obj):
        versicles = obj.versicle_set.all()
        if versicles:
            if len(books := set(str(versicle.book) for versicle in versicles)) > 1:
                chapters_per_book = ''
                for book in sorted(books, reverse=True):
                    book_versicles = versicles.filter(book__name=book.lower())
                    chapters = set(str(book_versicle.chapter) for book_versicle in book_versicles)
                    if not chapters_per_book:
                        chapters_per_book += ', '.join(sorted(chapters))
                    else:
                        chapters_per_book += ' - '
                        chapters_per_book += ', '.join(sorted(chapters))

                return chapters_per_book

            else:
                chapters = set(str(versicle.chapter) for versicle in versicles)
                return ', '.join(sorted(chapters))

        return 'N/A'

    chapters.short_description = 'capítulos'
