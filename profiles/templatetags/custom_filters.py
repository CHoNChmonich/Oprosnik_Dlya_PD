# Внутри вашего приложения создайте файл templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def dict_key(value, key):
    return value.get(key, '')
