from django import template

register = template.Library()


@register.filter
def return_index(lst, index):
    return lst[index]
