from django.shortcuts import render
from django.http import HttpResponseRedirect
from DRAGProj.forms.custominputform import CustomInputForm
from DRAGProj.forms.fitnessform import FitnessForm
import DRAG.datacontext as dc
import DRAGProj.dragcommon.formhelper as fh
import DRAGProj.geneticrunner as gr

def index(request):
    return render(request, "DRAG/index.html", {"is_home": True})

def fitness(request):
    if request.method == 'POST':
        form = FitnessForm(request.POST, size=dc.context["populationsize"])
        candidatefitnesses = []
        if form.is_valid():
            for fitness in form.collectfitnesses():
                candidatefitnesses.append(fitness[1])
            return HttpResponseRedirect('/RateFitness')
    else:
        form = FitnessForm(size=dc.context["populationsize"])

    dc.context["fitnessform"] = form
    return render(request, "DRAG/fitness.html", dc.context)

def firstfitness(request):
    context = dc.context
    bpm = context["bpm"]
    population = gr.initiliasepopulation(context["input"], context["genre"], bpm)
    gr.processinput(population, bpm)
    context["fitnessform"] = FitnessForm(size=context["populationsize"])
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
            return HttpResponseRedirect('/FirstFitness')

    else:
        form = CustomInputForm()

    dc.context["form"] = form
    return render(request, 'DRAG/startdiversify.html', dc.context)

