from django import template

register = template.Library()

@register.filter(name='to_int')
def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.simple_tag
def debug_tag():
    return "✔️ Custom tags loaded"
