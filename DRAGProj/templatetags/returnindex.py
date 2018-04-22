from django import template

"""
An extension module defining a filter for in Django html templates.

    Author:
        James

    Version:
        1.0.0

    See:
        django.template
"""

# Register any declared filters in the library.
register = template.Library()


@register.filter
def return_index(lst, index):
    """
    A filter to return a list element at a given index.

    Args:
        lst (:obj:`list`): The list to search.
        index (int): The index to return.

    Returns:
        The element at index in the list.
    """
    return lst[index]
