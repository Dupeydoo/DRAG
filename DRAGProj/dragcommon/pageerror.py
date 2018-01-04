from django.shortcuts import render
from DRAG.datacontext import context

"""
A module which catches errors which would cause problems if a DRAG page was 
accessed directly by URL.

    Author:
        James
        
    Version:
        1.1.0
"""


def catchkeyerror(request):
    """
    Represents an error when trying to access a page with required input.

    Args/Returns:
        See catchcriticalerror(request)
    """
    return catchcriticalerror(request)


def catchpreseterror(request):
    """
    Represents an error when trying to access the preset intermediary.

    Args/Returns:
        See catchcriticalerror(request)
    """
    return catchcriticalerror(request)


def catchcriticalerror(request):
    """
    Represents a critical generic errors.

    Args:
        request (:obj:`Request`): The request object associated with the page.

    Returns:
        :obj:`HTTPResponse`: A HTTPResponse object to the given page with the request and context.
    """
    return render(request, "DRAG/error.html", context)
