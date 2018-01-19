from django.http import HttpResponseRedirect

import DRAGNN.storage.datastore as ds
import DRAGProj.geneticrunner as gr
import DRAG.datacontext as dc

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


def perform_generation(form):
    """
    Performs a normal generation of the genetic algorithm.

    Args:
        form (:obj:`Form`): The fitness audio form.
    See:
        DRAG.datacontext
        DRAGProg.geneticrunner
    """
    context = dc.context
    gather_fitness_input(form.collect_fitnesses(), context["population"])
    ds.store_data(context["population"], ds.get_data_store())  # Write data to HDF5 for neural net later
    population = gr.perform_genetics(context["population"])  # start the genetic operations.
    context["population"] = population
    gr.clear_wav_files()
    gr.process_input(population, context["bpm"])  # clear up and rewrite the wav files.


def gather_fitness_input(dict, population):
    """
    Collects the fitness values from the fitness audio form and assigns
    them to the respective population members.

    Args:
        dict (:obj:`generator` of int): The generator object to access fitnesses from.
        population (:obj:`list` of :obj:`Track`): The Track population.
    """
    for counter, fitness in enumerate(dict):  # enumerate exposes a counter while allowing normal generator iteration.
        pop_member = population[counter]
        pop_member.fitness = fitness[1]  # get the fitness value and assign to a population member.


def generation_check(current_generation, max_generation):
    """
    Checks to see when manual generations have finished to begin Machine Learning.

    Args:
        current_generation (int): The current generation.
        max_generation (int): The maximum manual generations.

    Returns:
        HttpResponseRedirect (:obj:HTTPResponseRedirect): A redirect object to route to a different url.
    """
    return current_generation == max_generation
