import DRAGProj.generators.genregenerator as gg
from DRAGProj.dragcommon.track import Track

"""
This module contains functions to generate a population of Tracks for use in
the genetic algorithm.

    Author:
        James
    
    Version:
        3.4.2
        
    See:
        DRAGProj.generators.genregenerator
"""


def generatepopulation(psize, cratio, inputlist, genre, timesig):
    """
    This functions generates the population and returns it to the caller.

    Args:
        psize (int): The size of the population to be generated.
        cratio (float): The ratio of input copies to use.
        inputlist (:obj:`list` of int): The list of instrument ints to use as input.
        genre (:obj:`str`): The genre of the track to diversify.
        timesig (int): The time signature used in track generation.

    Returns:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
    """
    copyappend = int(cratio * psize)  # The number of copies to insert into the population.
    population = []

    population = populatecopies(population, copyappend, inputlist)  # Create the copies.
    population = generategenretracks(population, (psize - copyappend), genre, timesig)  # Add genre generated remainder.
    return population


def generategenretracks(population, tracknumber, genre, timesig):
    """
    Inspects the genre and generates the required genre tracks.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        tracknumber (int): The number of tracks to generate.
        genre (:obj:`str`): The genre of the track to diversify.
        timesig (int): The time signature used in track generation.

    Returns:
        population (:obj:`list` of :obj:`Track`): The population of tracks with genre tracks added.
    """
    if genre == "Rock":
        population = gg.generaterocktracks(population, tracknumber, timesig)

    elif genre == "Blues":
        population = gg.generatebluestracks(population, tracknumber, timesig)

    elif genre == "Jazz":
        population = gg.generatejazztracks(population, tracknumber, timesig)

    return population


def populatecopies(population, copynumber, inputlist):
    """
    Creates copies of the inputlist to fill the first generation.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        copynumber (int): The number of copies to generate.
        inputlist (:obj:`list` of int): The list of instrument ints to use as input.

    Returns:
        population (:obj:`list` of :obj:`Track`): The population of tracks with copies added.

    See:
        DRAGProj.dragcommon.track
    """
    for candidate in range(copynumber):
        track = Track(inputlist, 0)  # Create a new track.
        population.append(track)
    return population
