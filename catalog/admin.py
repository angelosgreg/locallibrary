from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Author, AuthorAdmin)
