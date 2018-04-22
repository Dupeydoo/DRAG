from DRAG.datacontext import context
from DRAGProj import geneticrunner as gr
import numpy as np

"""
The automatic generation module. When the classification module
has fitted a model this module uses it to predict fitness values
and perform many automatic GA generations.

    Author:
        James
        
    Version:
        2.0.0
"""


def run(model, request, hot_encoder):
    """
    Iterates single generations until all automatic generations
    have been performed.

    Args:
        model (:obj:`GridSearchCV`): The Random Forest Classifier
        wrapped in a GridSearchCV object.

        request (:obj:`Request`): The Request object containing the
        user_id.

        hot_encoder (:obj:`OneHotEncoder`): OHE object for categorical
        encoding.
    """
    for generation in range(context["automated_generations"]):
        request.session["current_generation"] += 1
        single_generation(model, request, hot_encoder)


def single_generation(model, request, hot_encoder):
    """
    Performs a single GA generation of the current user's population.

    Args:
        model (:obj:`GridSearchCV`): The Random Forest Classifier
        wrapped in a GridSearchCV object.

        request (:obj:`Request`): The Request object containing the
        user_id.

        hot_encoder (:obj:`OneHotEncoder`): OHE object for categorical
        encoding.
    """
    for track in context[request.session["user_id"] + "population"]:
        drums = np.array([track.content])

        # One hot encode the numpy drum array.
        content = hot_encoder.transform(drums).toarray()
        track.fitness = model.predict(content)

    # Call the genetic runner module to perform a generation.
    context[request.session["user_id"] + "population"] = gr.perform_genetics(
        context[request.session["user_id"] + "population"])
