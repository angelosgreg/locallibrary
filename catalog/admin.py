from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Genre)
# admin.site.register(BookInstance)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)
