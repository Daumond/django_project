from django import template

register = template.Library()


@register.simple_tag
def my_media(val):
    return f'/media/{val}'
