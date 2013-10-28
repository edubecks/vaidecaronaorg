# coding: utf-8
__author__ = 'edubecks'

from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)