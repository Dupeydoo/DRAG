from django.http import HttpResponseRedirect

import DRAGProj.geneticrunner as gr
import DRAG.datacontext as dc

from DRAGProj.dragcommon.track import Track

def performgeneration(form):
    context = dc.context
    gatherfitnessinput(form.collectfitnesses(), context["population"])
    population = gr.performgenetics(context["population"])
    context["population"] = population
    gr.clearwavfiles()
    gr.processinput(population, context["bpm"])

def gatherfitnessinput(dict, population):
    for counter, fitness in enumerate(dict):
        popmember = population[counter]
        popmember.fitness = fitness[1]

def generationcheck(currentgeneration, maxgeneration):
    if currentgeneration == maxgeneration:
        return HttpResponseRedirect('/NeuralNetwork')