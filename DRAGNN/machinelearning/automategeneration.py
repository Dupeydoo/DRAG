from DRAG.datacontext import context
from DRAGProj import geneticrunner as gr

from django.http import HttpResponseRedirect


def run(model, request):
    for generation in range(context["automated_generations"]):
        request.session["current_generation"] += 1
        single_generation(model, request)


def single_generation(model, request):
    for track in context[request.session["user_id"] + "population"]:
        predicted_fitness = model.predict([track.content])
        predicted_fitness = 0 if predicted_fitness < 0 else predicted_fitness
        track.fitness = int(predicted_fitness)
    context[request.session["user_id"] + "population"] = gr.perform_genetics(
        context[request.session["user_id"] + "population"])
