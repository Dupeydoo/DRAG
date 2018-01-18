from django.shortcuts import render
from DRAG.datacontext import context

from DRAGProj.dragcommon import pageerror as pe
from DRAGNN.machinelearning import linearregressiontest


def neuralnetwork(request):
    try:
        linearregressiontest.linearregression()
    except:
        return pe.catchkeyerror(request)
    return render(request, "neuralnetwork.html", context)
