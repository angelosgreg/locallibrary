from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

# admin.site.register(Genre)
# admin.site.register(BookInstance)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

admin.site.register(Author, AuthorAdmin)
