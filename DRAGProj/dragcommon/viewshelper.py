import uuid

import DRAGNN.storage.datastore as ds
import DRAGProj.geneticrunner as gr
import DRAGProj.dragcommon.wavbuilder as wb
import DRAG.datacontext as dc

from DRAGProj.models.anonymoususer import AnonymousUser

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


def perform_generation(form, request):
    """
    Performs a normal generation of the genetic algorithm.

    Args:
        form (:obj:`Form`): The fitness audio form.
    See:
        DRAG.datacontext
        DRAGProg.geneticrunner
    """
    population = dc.context[request.session["user_id"] + "population"]
    gather_fitness_input(form.collect_fitnesses(), population)
    ds.store_data(population, ds.get_data_store())  # Write data to HDF5 for neural net later
    population = gr.perform_genetics(population)  # start the genetic operations.
    dc.context[request.session["user_id"] + "population"] = population
    gr.process_input(population, request.session["bpm"], request)  # clear up and rewrite the wav files.


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


def set_uuid_cookie(response, request, cookie_uuid=None):
    if cookie_uuid is not None:
        cookie_uuid = str(cookie_uuid)
        user = AnonymousUser(UUID=cookie_uuid)

        if not AnonymousUser.objects.get_or_create(UUID=cookie_uuid)[1]:
            context = dc.context
            wb.clear_wav_candidates((context["system_path"] + context["wav_path"]), cookie_uuid)
            request.session["user_id"] = cookie_uuid
        else:
            new_uuid = generate_uuid(response, request)
            user = AnonymousUser(UUID=new_uuid)
            user.save()

    else:
        new_uuid = generate_uuid(response, request)
        user = AnonymousUser(UUID=new_uuid)
        user.save()


def generate_uuid(response, request):
    new_uuid = uuid.uuid1()
    new_uuid = str(new_uuid)
    response.set_cookie("track_identifier", new_uuid)
    request.session["user_id"] = new_uuid
    return new_uuid
