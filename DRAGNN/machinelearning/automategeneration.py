from DRAG.datacontext import context
from DRAGProj import geneticrunner as gr

from django.http import HttpResponseRedirect


def run(model):
    for generation in range(context["automated_generations"]):
        context["current_generation"] += 1
        single_generation(model)


def single_generation(model):
    for track in context["population"]:
        predicted_fitness = model.predict([track.content])
        predicted_fitness = 0 if predicted_fitness < 0 else predicted_fitness
        track.fitness = int(predicted_fitness)
    context["population"] = gr.perform_genetics(context["population"])
