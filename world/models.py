from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural='Страны'

class City(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')
    country = models.ForeignKey(Country, verbose_name='Страна')
    population = models.PositiveIntegerField(verbose_name='Численность')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural='Города'