from django.shortcuts import render
from DRAG.datacontext import context

def catchkeyerror(request):
    return render(request, "DRAG/error.html", context)