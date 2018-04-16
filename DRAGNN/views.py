from django.shortcuts import render
from django.http import HttpResponseRedirect
from DRAG.datacontext import context

from DRAGProj.dragcommon import pageerror as pe
from DRAGProj.dragcommon import viewshelper as vh

from DRAGNN.machinelearning import classification as cl
from DRAGNN.storage import datastore as ds


def machinelearn(request):
    vh.check_app_start(request)
    return render(request, "machinelearn.html", {"is_home": False})


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
    context["population_range"] = range(context["population_size"])
    if "user_id" not in request.session:
        ds.delete_data_store(request.session["user_id"])
    return render(request, "finish.html", context)
