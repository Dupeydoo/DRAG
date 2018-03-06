from django.shortcuts import render
from django.http import HttpResponseRedirect

from DRAGProj.forms.custominputform import CustomInputForm
from DRAGProj.forms.presetform import PresetForm
from DRAGProj.forms.fitnessform import FitnessForm

import DRAG.datacontext as dc
import DRAGProj.geneticrunner as gr

from DRAGProj.dragcommon.appstart import AppStart
import DRAGProj.dragcommon.formhelper as fh
import DRAGProj.dragcommon.pageerror as pe
import DRAGProj.dragcommon.viewshelper as vh

"""
Handles view and form logic within the DRAGProj application.
Every view function corresponds to a url pattern in DRAGProj.urls.py.

    Author:
        James
        
    Version:
        5.0.0
        
    See:
        django.shortcuts,
        django.http,
        DRAGProj.forms,
        DRAGProj.geneticrunner,
        DRAGProj.dragcommon,
        DRAG.datacontext
"""


def index(request):
    """
    View function for the index.html page.

    Args:
        request (:obj:`Request`): The Request object representing a HTTP request to a page.

    Returns:
        :obj:`HTTPResponse`: A HTTPResponse object to a page with the HTTP request and optional dictionary.
    """
    request.session.flush()
    AppStart.clear = False
    request.session["current_generation"] = 1  # Reset the generations if the user goes home mid-diversification.
    response = render(request, "DRAG/index.html", {"is_home": True})
    cookie_uuid = request.COOKIES["track_identifier"] if "track_identifier" in request.COOKIES else None
    vh.set_uuid_cookie(response, request, cookie_uuid)
    return response


def fitness(request):
    """
    View function for the fitness.html page.

    Args:
        request (:obj:`Request`): The Request object representing a HTTP request to a page.

    Returns:
        :obj:`HTTPResponse`: A HTTPResponse object to a page with the HTTP request and optional dictionary.
        :obj:`HTTPResponseRedirect`: A HTTPResponseRedirect object that redirects the user to the routed url.
    """
    vh.check_app_start(request)
    context = dc.context
    if request.method == 'POST':  # If the form has been submitted.
        form = FitnessForm(request.POST,
                           size=context["population_size"])  # Create a fitness form object with the POST data.

        if form.is_valid():  # If the data is valid perform a generation and redirect back here with a GET request.
            vh.perform_generation(form, request)
            return HttpResponseRedirect('/RateFitness')

    else:
        try:  # Here we check to see if the user is accessing the page correctly.
            bpm = request.session["bpm"]
            if vh.generation_check(request.session["current_generation"],
                                   context["manual_generations"]):  # See if its time to ANN.
                return HttpResponseRedirect("/MachineLearn")
            form = FitnessForm(size=context["population_size"])
            request.session["current_generation"] += 1  # increment the generations.

        except KeyError as k:  # If the user tries to access the page directly by url.
            return pe.catch_key_error(request)

    population = context[request.session["user_id"] + "population"]
    return render(request, "DRAG/fitness.html", {"fitness_form": form, "population": population, "is_home": False})


def first_fitness(request):
    """
    View function for the fitness.html page only accessed the first time.

    Args:
        request (:obj:`Request`): The Request object representing a HTTP request to a page.

    Returns:
        :obj:`HTTPResponse`: A HTTPResponse object to a page with the HTTP request and optional dictionary.
    """
    vh.check_app_start(request)
    context = dc.context
    try:
        bpm = request.session["bpm"]
        population = gr.initiliase_population(request.session["input"],
                                              request.session["genre"])  # Initialise the population.
        gr.process_input(population, bpm, request)
        fitness_form = FitnessForm(size=context["population_size"])  # Create a fitness form to use.
        context[request.session["user_id"] + "population"] = population  # Reassign the population.
        return render(request, "DRAG/fitness.html",
                      {"fitness_form": fitness_form, "population": population, "is_home": False})

    except KeyError as k:
        return pe.catch_key_error(request)


def diversify(request):
    """
    View function for the startdiversify.html page.

    Args:
        request (:obj:`Request`): The Request object representing a HTTP request to a page.

    Returns:
        :obj:`HTTPResponse`: A HTTPResponse object to a page with the HTTP request and optional dictionary.
    """
    if request.method == 'POST':
        form = CustomInputForm(request.POST)  # Make an input form.

        if form.is_valid():
            request.session["genre"] = form.cleaned_data["genre"]
            request.session["bpm"] = form.cleaned_data["bpm"]
            request.session["input"] = fh.construct_input(
                form.cleaned_data)  # Get all the clean data from the POST form.
            return HttpResponseRedirect('/FirstFitness')  # Proceed to rate the fitness.

    else:
        form = CustomInputForm()
        preset = PresetForm()  # On GET initialise both forms.

    preset = preset if "preset" in locals() else PresetForm()
    return render(request, 'DRAG/startdiversify.html', {"preset": preset, "form": form, "is_home": False})


def preset(request):
    """
    View function for the preset url route.

    Args:
        request (:obj:`Request`): The Request object representing a HTTP request to a page.

    Returns:
        :obj:`HTTPResponse`: A HTTPResponse object to a page with the HTTP request and optional dictionary.
    """
    if request.method == 'POST':
        form = PresetForm(request.POST)

        if form.is_valid():
            request.session["bpm"] = form.cleaned_data["bpm"]
            request.session["input"] = fh.get_preset(form.cleaned_data["preset"])
            request.session["genre"] = "Rock"  # As before get the cleaned form POST data.
            return HttpResponseRedirect('/FirstFitness')  # Proceed to rate tracks.

    else:
        return pe.catch_preset_error(request)

    return render(request, 'DRAG/startdiversify.html')


def error(request):
    """
    View function for the error.html page. Deals with errors from incorrectly accessing
    pages.

    Args:
        request (:obj:`Request`): The Request object representing a HTTP request to a page.

    Returns:
        :obj:`HTTPResponse`: A HTTPResponse object to a page with the HTTP request and optional dictionary.
    """
    response = render(request, 'DRAG/error.html', dc.context)
    cookie_uuid = request.COOKIES["track_identifier"]
    vh.set_uuid_cookie(response, request, cookie_uuid)
    return response


def about(request):
    """
    View function for the about page.

    Args:
        request (:obj:`Request`): The Request object representing a HTTP request to a page.

    Returns:
        :obj:`HTTPResponse`: A HTTPResponse object to a page with the HTTP request and optional dictionary.
    """
    request.session.flush()
    return render(request, 'DRAG/about.html', {"is_home": False})


def faq(request):
    """
    View function for the faq page.

    Args:
        request (:obj:`Request`): The Request object representing a HTTP request to a page.

    Returns:
        :obj:`HTTPResponse`: A HTTPResponse object to a page with the HTTP request and optional dictionary.
    """
    request.session.flush()
    return render(request, 'DRAG/faq.html', {"is_home": False})


def page_not_found_error(request):
    """
    View function for the 404 status code page.

    Args:
        request (:obj:`Request`): The Request object representing a HTTP request to a page.

    Returns:
        :obj:`HTTPResponse`: A HTTPResponse object to a page with the HTTP request and optional dictionary.
    """
    request.session.flush()
    return render(request, 'DRAG/404.html', {"is_home": True})


def server_error(request):
    """
    View function for the 500 status code page.

    Args:
        request (:obj:`Request`): The Request object representing a HTTP request to a page.

    Returns:
        :obj:`HTTPResponse`: A HTTPResponse object to a page with the HTTP request and optional dictionary.
    """
    request.session.flush()
    return render(request, 'DRAG/500.html', {"is_home": True})
