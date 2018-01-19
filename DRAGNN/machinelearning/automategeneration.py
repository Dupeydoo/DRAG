from DRAG.datacontext import context
from DRAGProj import geneticrunner as gr

from django.http import HttpResponseRedirect


def run(model):
    for generation in range(context["automatedgenerations"]):
        context["currentgeneration"] += 1
        singlegeneration(model)
    return HttpResponseRedirect("/Finished")


def singlegeneration(model):
    for track in context["population"]:
        predictedfitness = model.predict([track.content])
        track.fitness = int(predictedfitness)
    context["population"] = gr.performgenetics(context["population"])
