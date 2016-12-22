from django.contrib import admin

# Register your models here.
from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'born')

# class AuthorInline(admin.StackedInline):
#     model = Author

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title', 'year', 'isbn')
    filter_horizontal=('authors',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
