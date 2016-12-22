# -*- coding: utf-8 -*-
'''
Created on 20 дек. 2016 г.
Заполняет таблицы world_county, world_city на основе файлов countries.txt, cities.txt
@author: igor
'''
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from world.models import City, Country
from django.db import transaction

def main():
    with transaction.atomic():
        with open('new_countries.txt', 'r') as fd:
            countries = {}
            for line in fd:
                _id, name = line.strip().split('\t')
                _id = int(_id)
                country = Country(name=name)
                country.save()
                if country.id != _id:
                    raise RuntimeError('%s не совпадают id: %d!=%d' % (name, country.id, _id))
                countries[country.id] = country
        with open('new_cities.txt', 'r') as fd:
            for line in fd:
                _id, name, country_id, population = line.strip().split('\t')
                _id = int(_id)
                population = int(population)
                country_id = int(country_id)
                city = City(name = name, country = countries[country_id], population=population)
                city.save()
                if city.id != _id:
                    raise RuntimeError('%s не совпадают id: %d!=%d' % (name, city.id, _id))

if __name__ == '__main__':
    main()


