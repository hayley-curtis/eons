from django import template

register = template.Library()

#must load filter file in template when used e.g. {% load asterisms_extra_filters %}
@register.filter()
def rem_desig(value):
    value = str(value)
    value = value[:-4]
    return value.title()

