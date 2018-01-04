from django.shortcuts import render
from DRAG.datacontext import context

def catchkeyerror(request):
    return catchcriticalerror(request)

def catchpreseterror(request):
    return catchcriticalerror(request)

def catchcriticalerror(request):
    return render(request, "DRAG/error.html", context)