from django.http import HttpResponseRedirect

import DRAGProj.geneticrunner as gr
import DRAG.datacontext as dc

from DRAGProj.dragcommon.track import Track

"""
This module provides assisting functions to views.py to keep the views logic
isolated.

    Author:
        James
    
    Version:
        1.5.2
        
    See:
        DRAGProj.views
"""


def performgeneration(form):
    """
    Performs a normal generation of the genetic algorithm.

    Args:
        form (:obj:`Form`): The fitness audio form.
    See:
        DRAG.datacontext
        DRAGProg.geneticrunner
    """
    context = dc.context
    gatherfitnessinput(form.collectfitnesses(), context["population"])
    population = gr.performgenetics(context["population"])  # start the genetic operations.
    context["population"] = population
    gr.clearwavfiles()
    gr.processinput(population, context["bpm"])  # clear up and rewrite the wav files.


def gatherfitnessinput(dict, population):
    """
    Collects the fitness values from the fitness audio form and assigns
    them to the respective population members.

    Args:
        dict (:obj:`generator` of int): The generator object to access fitnesses from.
        population (:obj:`list` of :obj:`Track`): The Track population.
    """
    for counter, fitness in enumerate(dict):  # enumerate exposes a counter while allowing normal generator iteration.
        popmember = population[counter]
        popmember.fitness = fitness[1]  # get the fitness value and assign to a population member.


def generationcheck(currentgeneration, maxgeneration):
    """
    Checks to see when manual generations have finished to begin Machine Learning.

    Args:
        currentgeneration (int): The current generation.
        maxgeneration (int): The maximum manual generations.

    Returns:
        HttpResponseRedirect (:obj:HTTPResponseRedirect): A redirect object to route to a different url.
    """
    if currentgeneration == maxgeneration:
        return HttpResponseRedirect('/NeuralNetwork')  # Redirect to the Machine Learning app, DRAGNN.
