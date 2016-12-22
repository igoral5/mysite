from django.contrib import admin

# Register your models here.
from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'born')


class AuthorInline(admin.TabularInline):
    model = Book.authors.through
    extra = 0
    verbose_name='Автор'
    verbose_name_plural='Авторы'
     
    
    

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'isbn')
    exclude = ('authors',)
    inlines = (AuthorInline,)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
