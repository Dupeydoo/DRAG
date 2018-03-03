from django.shortcuts import render
from django.http import HttpResponseRedirect
from DRAG.datacontext import context

from DRAGProj.dragcommon import pageerror as pe
from DRAGProj.dragcommon import viewshelper as vh


def machinelearn(request):
    vh.check_app_start(request)
    try:
        bpm = request.session["bpm"]
        print("Hello")
    except KeyError as k:
        return pe.catch_key_error(request)
    return HttpResponseRedirect("/Finished")


def finished(request):
    if request.session["current_generation"] != context["manual_generations"] + context["automated_generations"]:
        return pe.catch_critical_error(request)
    return render(request, "finish.html", context)
