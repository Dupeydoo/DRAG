import DRAGProj.generators.populationgenerator as pg
import DRAGProj.dragcommon.wavbuilder as wb
import DRAGProj.dragcommon.dragmaths as dm
import DRAG.datacontext as dc

from DRAGProj.geneticoperations import selection
from DRAGProj.geneticoperations import crossover
from DRAGProj.geneticoperations import mutation
from DRAGProj.geneticoperations import generationalreplacement

"""
This module provides the main running functions of the genetic algorithm.

    Author:
        James
        
    Version:
        4.3.3
        
    See:
        DRAG.datacontext,
        DRAGProj.geneticoperations,
        DRAGProj.generators,
        DRAGProj.dragcommon
"""

context = dc.context
"""context (:obj:`dict`): The datacontext containing the genetic algorithm parameters."""

system_path = context["system_path"]
"""system_path (:obj:`str`): The string representing the path of the webserver."""

wav_path = context["wav_path"]
"""wav_path (:obj:str): The string representing the path of the wav files."""

population_size = context["population_size"]
"""population_size (int): The size of the population to generate."""

copy_ratio = context["copy_ratio"]
"""copy_ratio (int): The number of input copies to generate."""

tournament_size = context["tournament_size"]
"""tournament_size (int): The tournament size parameter used in tournament selection."""

time_signature = context["time_signature"]
"""time_signature (int): The time signature of the output tracks."""

cross_prob = context["cross_prob"]
"""cross_prob (float): The probability of genetic crossover occuring."""

muta_prob = context["muta_prob"]
"""muta_prob (float): The probability of genetic mutation occuring."""

DEFAULT_POP_SIZE = 10
"""DEFAULT_POP_SIZE (int): A default population size constant for incorrect population sizes."""


def initiliase_population(input_list, genre):
    """
    Initialises the first population.

    Args:
        input_list (:obj:`list` of int): The drum list input to the algorithm.
        genre (:obj:`str`): The genre of the tracks to diversify.

    Returns:
        :obj:`list` of :obj:`Track`: The initial population.
    """
    if dm.is_even(population_size) and population_size >= 0:  # Genetic crossover takes place on pairs.
        return pg.generate_population(population_size, copy_ratio, input_list, genre, time_signature)
    else:
        pop_size = DEFAULT_POP_SIZE  # If incorrect input is set for whatever reason, assume a default.
        return pg.generate_population(pop_size, copy_ratio, input_list, genre, time_signature)


def process_input(population, bpm, request):
    """
    Initiates the wav file creation process.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        bpm (int): A number representing the beats per minute or tempo of the track.
        request (:obj:`HTTPRequest`): The request asking for tracks to be generated.
    """
    path = system_path + wav_path                       # Get the full path to write files to.
    for candidate in range(len(population)):
        solution = population[candidate]
        output_file = path + request.session["user_id"] + "candidate" + str(
            candidate) + ".wav"                         # Build unique candidate file names
        wb.map_input(solution, bpm, output_file, path)  # Write the wav files.


def perform_genetics(population):
    """
    Performs the genetic operations.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.

    Returns:
        new_population (:obj:`list` of :obj:`Track`): The new population of tracks.
    """
    parents = selection.do_selection(population, tournament_size)
    children = crossover.do_crossover(parents, cross_prob)
    children = mutation.do_mutation(children, muta_prob)
    new_population = generationalreplacement.do_replacement(population, children)
    return new_population


def clear_wav_files():
    """
    Helper to call the wavbuilder clear_wav_candidates(path, string)
    """
    path = system_path + wav_path
    wb.clear_wav_candidates(path, "candidate")
