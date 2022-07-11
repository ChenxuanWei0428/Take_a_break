from django import template

register = template.Library()

@register.simple_tag
def reset_index(index):
    index = 0
    return None

@register.simple_tag
def update_index(index, value):
    index = value
    return index

# removed for now