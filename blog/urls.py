'''
Created on 21 дек. 2016 г.

@author: igor
'''
from django.conf.urls import url
from .views import archive

urlpatterns = [
    url(r'^$', archive, name='archve'),
]