from django.shortcuts import render
from DRAG.datacontext import context

from DRAGProj.dragcommon import pageerror as pe
from DRAGNN.machinelearning import regression


def machinelearn(request):
    try:
        regression.linearregression()
    except KeyError as k:
        return pe.catchkeyerror(request)
    return render(request, "machinelearn.html", context)


def finished(request):
    if context["currentgeneration"] != context["manualgenerations"] + context["automatedgenerations"]:
        return pe.catchcriticalerror(request)
    return render(request, "finish.html", context)
