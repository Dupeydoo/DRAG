from django.http import HttpResponseRedirect
from django.shortcuts import render

from DRAG.datacontext import context
from DRAGNN.machinelearning import classification as cl
from DRAGNN.storage import datastore as ds
from DRAGProj.dragcommon import pageerror as pe
from DRAGProj.dragcommon import viewshelper as vh

"""
Handles view logic within the DRAGNN application. Every view 
function corresponds to a url pattern in DRAGNN.urls.py.

    Author:
        James

    Version:
        2.0.0
        
    See:
        django.shortcuts
        django.http
        DRAG.datacontext
        DRAGNN.machinelearning
        DRAGNN.storage
        
"""


def machinelearn(request):
    """
    View function mapped to the MachineLearn URL route. Returns
    the page where the machine learning is initiated by pressing
    a button on the page.

    Args:
        request (:obj:`Request`): The web request to the URL route.

    Returns:
        :obj:`HTTPResponse`: A HTTPResponse object to the machinelearn.html
        page.
    """
    vh.check_app_start(request)
    return render(request, "machinelearn.html", {"is_home": False})


def machineload(request):
    """
    View function that maps to the MachineLoad URL route. Here javascript
    is used to show a loading screen. While this happens the machine learning
    process is executed.

    Args:
        request (:obj:`Request`): The web request to the URL route.

    Returns:
        :obj:`HTTPResponseRedirect`: A redirect to the Finished page.
    """
    vh.check_app_start(request)
    try:
        # Check a parameter has been set and perform classification.
        bpm = request.session["bpm"]
        cl.classification(request, request.session["user_id"])

    except KeyError as k:
        return pe.catch_key_error(request)
    return HttpResponseRedirect("/Finished")


def finished(request):
    """
    View function that maps to the Finished URL route. Called when the
    machine leaning phase has concluded.

    Args:
        request (:obj:`Request`): The web request to the URL route.

    Returns:
        :obj:`HTTPResponse`: A HTTPResponse object to the finish.html page.
    """
    # Check that all the planned generations have been fulfilled.
    if request.session["current_generation"] != context["manual_generations"] \
            + context["automated_generations"]:
        return pe.catch_critical_error(request)

    # Expose a range value used to display tracks in the Django template.
    context["population_range"] = range(context["population_size"])

    # Delete the data store for next time.
    ds.delete_data_store(request.session["user_id"])
    return render(request, "finish.html", context)
