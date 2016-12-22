# -*- coding: utf-8 -*-
'''
Created on 21 дек. 2016 г.
Сохраняет таблицы world_city, world_country в текстовые файлы
@author: igor
'''
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from world.models import City

def main():
    with open('new_cities.txt', 'w') as fd:
        countries = {}
        for city in City.objects.all().order_by('id'):
            print(city.id, city.name, city.country.id, city.population, sep='\t', file=fd)
            countries[city.country.id] = city.country
    with open('new_countries.txt', 'w') as fd:
        for country_id in sorted(countries.keys()):
            print(country_id, countries[country_id].name, sep='\t', file=fd)

if __name__ == '__main__':
    main()
        
