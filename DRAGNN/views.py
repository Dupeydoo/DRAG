from django.shortcuts import render
from django.http import HttpResponseRedirect
from DRAG.datacontext import context

from DRAGProj.dragcommon import pageerror as pe
from DRAGNN.machinelearning import regression


def machinelearn(request):
    try:
        regression.linear_regression()
    except KeyError as k:
        return pe.catch_key_error(request)
    return HttpResponseRedirect("/Finished")


def finished(request):
    if context["current_generation"] != context["manual_generations"] + context["automated_generations"]:
        return pe.catch_critical_error(request)
    return render(request, "finish.html", context)
