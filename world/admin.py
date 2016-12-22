from django.contrib import admin

# Register your models here.

from .models import City, Country

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'population')

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)