from django.contrib import admin
from .models import Book, BookInstance, Author, Genre, Language

class BookInline(admin.TabularInline):
    model=Book

class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ('first_name', 'last_name', ('date_of_birth', 'date_of_death'))
    inlines=[BookInline]
# Register your models here.
admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    model=BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','borrower','due_back','id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields':('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields':('status', 'due_back','borrower')
        }),
    )

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

#admin.site.register(models.Author)
#admin.site.register(models.Book)
#admin.site.register(models.BookInstance)
#admin.site.register(models.Genre)
#admin.site.register(models.Language)