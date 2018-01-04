from django.shortcuts import render
from DRAG.datacontext import context

def neuralnetwork(request):
    return render(request, "neuralnetwork.html", context)
