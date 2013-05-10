# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import template
from django.conf import settings

import datetime
from api.api import Yandexapi

API_KEY = getattr(settings, 'API_KEY')

register = template.Library()

@register.tag(name='current_time')
def current_time(parser, token):
    try:
        tag_name, format_string = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.contents[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format_string[1:-1])

class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = format_string

    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)

@register.tag(name='static_map_a')
def static_map_a(parser, token):
    try:
        tag_name, address, width, height, mode = token.split_contents()
    except ValueError:
        msg = '%r tag requires 4 args' % token.split_contents[0]
        raise template.TemplateSyntaxError(msg)
    return StaticMapA(address[1:-1], int(width), int(height), mode[1:-1])


class StaticMapA(template.Node):
    def __init__(self, address, width, height, mode = None):
        self.__address = address
        self.__width = width
        self.__height = height
        self.__mode = mode

    def render(self, context):
        api = Yandexapi(API_KEY)
        point = api.geocode(self.__address)
        url = Yandexapi.getStaticMapUrlParams(point, self.__width, self.__height, self.__mode)
        return '<img src=%s width=%s height=%s/>' % (url, self.__width, self.__height)

