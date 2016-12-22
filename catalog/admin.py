from django.contrib import admin

# Register your models here.
from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'born')


class AuthorInline(admin.StackedInline):
    model = Book.authors.through
    max_num = 1 
    
    

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'isbn')
    exclude = ('authors',)
    inlines = (AuthorInline,)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
