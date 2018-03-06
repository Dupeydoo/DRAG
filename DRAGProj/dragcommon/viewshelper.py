import uuid

import DRAGNN.storage.datastore as ds
import DRAGProj.geneticrunner as gr
import DRAGProj.dragcommon.wavbuilder as wb
import DRAG.datacontext as dc

from DRAGProj.models.anonymoususer import AnonymousUser
from DRAGProj.dragcommon.appstart import AppStart

"""
This module provides assisting functions to views.py to keep the views logic
isolated.

    Author:
        James
    
    Version:
        2.0.1
        
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
    # ds.store_data(population, request.session["user_id"])  # Write data to HDF5 for neural net later

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
        HttpResponseRedirect (:obj:`HTTPResponseRedirect`): A redirect object to route to a different url.
    """
    return current_generation == max_generation


def set_uuid_cookie(response, request, cookie_uuid=None):
    """
    Checks if the user has a cookie id, if they do, it checks if it is a valid id.
    Issues a new cookie in all events other than a valid id.

    Args:
        response (:obj:`HTTPResponse`): HTTP response to bind the cookie to.
        request (:obj:`HTTPRequest`): HTTP request that the user made.
        cookie_uuid (:obj:`Unknown`): The id value read off the user's cookie.
    """
    if cookie_uuid is not None:
        cookie_uuid = str(cookie_uuid)

        # If the user with the id doesn't need to be created, we know it exists.
        if not AnonymousUser.objects.get_or_create(UUID=cookie_uuid)[1]:
            context = dc.context
            wb.clear_wav_candidates((context["system_path"] + context["wav_path"]), cookie_uuid)
            request.session["user_id"] = cookie_uuid
        else:
            new_uuid = generate_uuid(response, request)
            create_user(new_uuid)

    # Issue a new cookie if no id is provided.
    else:
        new_uuid = generate_uuid(response, request)
        create_user(new_uuid)


def generate_uuid(response, request):
    """
    Generates a uuid to use as an anonymous user id and  sets a cookie with it.
    The id is also saved to the current session.

    Args:
        response (:obj:`HTTPResponse`): HTTP response to bind the cookie to.
        request (:obj:`HTTPRequest`): HTTP request that the user made.

    Returns:
        new_uuid (:obj:`str`): The generated uuid.
    """
    new_uuid = uuid.uuid1()  # The uuid1 method generates an identifier based on current time and randomness.
    new_uuid = str(new_uuid)
    response.set_cookie("track_identifier", new_uuid)
    request.session["user_id"] = new_uuid
    return new_uuid


def create_user(user_uuid):
    """
    Creates a new anonymous user and saves them to the database.

    Args:
         user_uuid (:obj:`str`): The id to use for the anonymous user.
    """
    user = AnonymousUser(UUID=user_uuid)
    user.save()


def check_app_start(request):
    if AppStart.clear:
        request.session.flush()
