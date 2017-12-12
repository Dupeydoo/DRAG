from django.shortcuts import render
from DRAGProj.custominputform import CustomInputForm
from django.http import HttpResponseRedirect
import DRAG.datacontext as dc
import DRAGProj.dragcommon.formhelper as fh

def index(request):
    return render(request, 'DRAG/index.html', {"is_home": True})

def fitness(request):
    return render(request, "DRAG/fitness.html", dc.context)

def diversify(request):
    if request.method == 'POST':
        form = CustomInputForm(request.POST)
        if form.is_valid():
            genre = form.cleaned_data["genre"]
            bpm = form.cleaned_data["bpm"]
            input = fh.constructinput(form.cleaned_data)
            dc.context["genre"] = genre
            dc.context["bpm"] = bpm
            dc.context["input"] = input
            return HttpResponseRedirect('/RateFitness')

    else:
        form = CustomInputForm()

    dc.context["form"] = form
    return render(request, 'DRAG/startdiversify.html', dc.context)

