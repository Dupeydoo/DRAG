from django import template

register = template.Library()


@register.filter
def strconcat(string, anotherstring):
    return str(string) + str(anotherstring)
