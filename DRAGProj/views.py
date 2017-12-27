from django.shortcuts import render
from django.http import HttpResponseRedirect

from DRAGProj.forms.custominputform import CustomInputForm
from DRAGProj.forms.fitnessform import FitnessForm

import DRAG.datacontext as dc
import DRAGProj.geneticrunner as gr

import DRAGProj.dragcommon.formhelper as fh
import DRAGProj.dragcommon.pageerror as pe
import DRAGProj.dragcommon.viewshelper as vh


def index(request):
    dc.context["currentgeneration"] = 1
    gr.clearwavfiles()
    return render(request, "DRAG/index.html", {"is_home": True})

def fitness(request):
    context = dc.context
    if request.method == 'POST':
        form = FitnessForm(request.POST, size=context["populationsize"])
        if form.is_valid():
            candidatefitnesses = vh.gatherfitnessinput(form.collectfitnesses())
            population = gr.performgenetics(context["population"], candidatefitnesses)
            context["population"] = population
            gr.clearwavfiles()
            gr.processinput(population, context["bpm"])
            return HttpResponseRedirect('/RateFitness')
    else:
        try:
            bpm, population = context["bpm"], context["population"]
            if context["currentgeneration"] == context["manualgenerations"]:
                return HttpResponseRedirect('/NeuralNetwork')
            context["currentgeneration"] = context["currentgeneration"] + 1
            form = FitnessForm(size=context["populationsize"])
        except KeyError as k:
            return pe.catchkeyerror(request)

    context["fitnessform"] = form
    return render(request, "DRAG/fitness.html", context)

def firstfitness(request):
    context = dc.context
    try:
        bpm = context["bpm"]
        population = gr.initiliasepopulation(context["input"], context["genre"], bpm)
        gr.processinput(population, bpm)
        context["fitnessform"] = FitnessForm(size=context["populationsize"])
        context["population"] = population
        return render(request, "DRAG/fitness.html", dc.context)
    except KeyError as k:
        return pe.catchkeyerror(request)



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

def neuralnetwork(request):
    context = dc.context
    try:
        bpm, population = context["bpm"], context["population"]
    except KeyError as k:
        return pe.catchkeyerror(request)
    return render(request, 'DRAG/neuralnetwork.html', context)

def error(request):
    return render(request, 'DRAG/error.html', dc.context)



