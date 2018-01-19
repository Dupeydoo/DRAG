from DRAG.datacontext import context
from DRAGProj import geneticrunner as gr

from django.http import HttpResponseRedirect


def run(model):
    for generation in range(context["automatedgenerations"]):
        context["currentgeneration"] += 1
        single_generation(model)
    return HttpResponseRedirect("/Finished")


def single_generation(model):
    for track in context["population"]:
        predicted_fitness = model.predict([track.content])
        track.fitness = int(predicted_fitness)
    context["population"] = gr.perform_genetics(context["population"])
