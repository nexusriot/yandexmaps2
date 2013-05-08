# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import template

import datetime

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


