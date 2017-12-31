from django.http import HttpResponseRedirect

import DRAGProj.geneticrunner as gr
import DRAG.datacontext as dc

def performgeneration(form):
    context = dc.context
    candidatefitnesses = gatherfitnessinput(form.collectfitnesses())
    population = gr.performgenetics(context["population"], candidatefitnesses)
    context["population"] = population
    gr.clearwavfiles()
    gr.processinput(population, context["bpm"])

def gatherfitnessinput(dict):
    candidatefitnesses = []
    for fitness in dict:
        candidatefitnesses.append(fitness[1])
    return candidatefitnesses

def generationcheck(currentgeneration, maxgeneration):
    if currentgeneration == maxgeneration:
        return HttpResponseRedirect('/NeuralNetwork')