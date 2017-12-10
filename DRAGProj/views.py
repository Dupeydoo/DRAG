from django.shortcuts import render
import DRAG.datacontext as dc


def index(request):
    return render(request, 'DRAG/index.html')


def diversify(request):
    return render(request, 'DRAG/startdiversify.html', dc.context)

def collectinput(request):
    return render(request, 'DRAG/startdiversify.html', dc.context)
