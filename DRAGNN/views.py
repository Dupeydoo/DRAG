from django.shortcuts import render
from django.http import HttpResponseRedirect
from DRAG.datacontext import context

from DRAGProj.dragcommon import pageerror as pe
from DRAGProj.dragcommon import viewshelper as vh

from DRAGNN.machinelearning import classification as cl


def machinelearn(request):
    vh.check_app_start(request)
    return render(request, "machinelearn.html")


def machineload(request):
    vh.check_app_start(request)
    try:
        bpm = request.session["bpm"]
        cl.classification(request, request.session["user_id"])

    except KeyError as k:
        return pe.catch_key_error(request)
    return HttpResponseRedirect("/Finished")


def finished(request):
    if request.session["current_generation"] != context["manual_generations"] + context["automated_generations"]:
        return pe.catch_critical_error(request)
    return render(request, "finish.html", context)
