from django import template

register = template.Library()


@register.simple_tag
def edit_link(value):
    return value.lower()
