# -*- coding: utf-8 -*-

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from __future__ import unicode_literals
#from django.utils.encoding import python_2_unicode_compatible

# TODO: Django on python 2 and 3 importing app differences
try:
    from point import Point
    from api import Yandexapi
except ImportError:
    from api.point import Point
    from api.api import Yandexapi

from django.test import TestCase
from django.conf import settings

API_KEY = getattr(settings, 'API_KEY')

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class ApiTest(TestCase):
    def test_geocoding(self):
        address = 'Москва, Большая Якиманка, 22'
        point = Point(37.614545, 55.738216)
        api = Yandexapi(API_KEY)
        result = api.geocode(address)
        self.assertEqual(point, result, None)

    def test_reverse(self):
        point = Point(37.521309,55.753134)
        address = 'Москва, Шелепихинская набережная, 12'
        api = Yandexapi(API_KEY)
        result = api.reverse(point)
        self.assertEqual(address, result, None)

    def test_staticMapP(self):
        point = Point(37.521309,55.753134)
        link = 'http://static-maps.yandex.ru/1.x/?ll=37.5213090,55.7531340&size=400,400&l=map&spn=0.003,0.003'
        result = Yandexapi.getStaticMapUrlParams(point, 400, 400)
        self.assertEqual(link, result)


