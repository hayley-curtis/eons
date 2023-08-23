from django import template

register = template.Library()

#must load filter file in template when used e.g. {% load asterisms_extra_filters %}
@register.filter()
def name_format(value):
    value = str(value)
    value = value.replace("_", " ")
    return value.title() 