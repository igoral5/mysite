from django.db import models

# Create your models here.

class Author(models.Model):
    last_name = models.CharField(max_length=100, blank=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    middle_name = models.CharField(max_length=100, blank=True, verbose_name='Отчество')
    born = models.DateField(verbose_name='Дата рождения')
    
    def __str__(self):
        name = [self.last_name]
        if self.first_name:
            name.append(self.first_name)
        if self.middle_name:
            name.append(self.middle_name)
        return ' '.join(name)
    
    class Meta:
        verbose_name='Автор'
        verbose_name_plural='Авторы'

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    year = models.PositiveIntegerField(verbose_name='Год издания')
    isbn = models.CharField(max_length=25, verbose_name='ISBN:')
    authors = models.ManyToManyField(Author, verbose_name='Автор(ы)')
    
    def __str__(self):
        return '%s %d г.' % (self.title, self.year)
    
    class Meta:
        verbose_name='Книга'
        verbose_name_plural='Книги'
