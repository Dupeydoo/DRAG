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

systempath = context["systempath"]
"""systempath (:obj:`str`): The string representing the path of the webserver."""

wavpath = context["wavpath"]
"""wavpath (:obj:str): The string representing the path of the wav files."""

populationsize = context["populationsize"]
"""populationsize (int): The size of the population to generate."""

copyratio = context["copyratio"]
"""copyratio (int): The number of input copies to generate."""

tournamentsize = context["tournamentsize"]
"""tournamentsize (int): The tournament size parameter used in tournament selection."""

timesignature = context["timesignature"]
"""timesignature (int): The time signature of the output tracks."""

crossprob = context["crossprob"]
"""crossprob (float): The probability of genetic crossover occuring."""

mutaprob = context["mutaprob"]
"""mutaprob (float): The probability of genetic mutation occuring."""


def initiliasepopulation(inputlist, genre):
    """
    Initialises the first population.

    Args:
        inputlist (:obj:`list` of int): The drum list input to the algorithm.
        genre (:obj:`str`): The genre of the tracks to diversify.

    Returns:
        :obj:`list` of :obj:`Track`: The initial population.
    """
    if dm.iseven(populationsize) and populationsize >= 0:  # Genetic crossover takes place on pairs.
        return pg.generatepopulation(populationsize, copyratio, inputlist, genre, timesignature)
    else:
        popsize = 20  # If incorrect input is set for whatever reason, assume a default.
        return pg.generatepopulation(popsize, copyratio, inputlist, genre, timesignature)


def processinput(population, bpm):
    """
    Initiates the wav file creation process.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        bpm (int): A number representing the beats per minute or tempo of the track.
    """
    path = systempath + wavpath  # Get the full path to write files to.
    for candidate in range(len(population)):
        solution = population[candidate]
        outputfile = path + "candidate" + str(candidate) + ".wav"  # Build unique candidate file names
        wb.mapinput(solution, bpm, outputfile, path)  # Write the wav files.


def performgenetics(population):
    """
    Performs the genetic operations.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.

    Returns:
        newpopulation (:obj:`list` of :obj:`Track`): The new population of tracks.
    """
    parents = selection.doselection(population, tournamentsize)
    children = crossover.docrossover(parents, crossprob)
    children = mutation.domutation(children, mutaprob)
    newpopulation = generationalreplacement.doreplacement(population, children)
    return newpopulation


def clearwavfiles():
    """
    Helper to call the wavbuilder clearwavcandidates(path, string)
    """
    path = systempath + wavpath
    wb.clearwavcandidates(path, "candidate")
