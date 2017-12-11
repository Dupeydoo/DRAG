from django.shortcuts import render
from DRAGProj.custominputform import CustomInputForm
from django.http import HttpResponseRedirect
import DRAG.datacontext as dc

def index(request):
    return render(request, 'DRAG/index.html', {"is_home": True})

def diversify(request):
    if request.method == 'POST':
        form = CustomInputForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/Diversify')

    else:
        form = CustomInputForm(initial={"custombeat": "Select an instruments/s"})

    dc.context["form"] = form
    return render(request, 'DRAG/startdiversify.html', dc.context)

