import random
from operator import itemgetter

from DRAGProj.dragcommon.track import Track

"""
The selection module performs tournament selection for the genetic algorithm.

    Author:
        James
        
    Version:
        2.0.0
"""


def doselection(population, tournamentsize):
    """
    Entry point function for selection.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        tournamentsize (int): Tournament size parameter used to control selection.

    Returns:
        parents (:obj:`list` of :obj:`Track`): The new population of tracks selected from the old.
    """
    parents = []
    for selections in range(len(population)):
        parent = tournamentselect(population, tournamentsize)  # Perform torunament selection.
        parent.hasChanged = False  # Nullify changes from last generation.
        parents.append(parent)
    return parents


def tournamentselect(population, tournamentsize):
    """
    Performs tournament selection.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        tournamentsize (int): Tournament size parameter used to control selection.

    Returns:
        :obj:`Track`: A track that has been selected from a tournament.
    """
    randomselections = []
    for candidates in range(tournamentsize):
        randindex = random.randrange(0, len(population))  # Pick a random index
        randomselections.append((randindex, population[randindex].fitness))  # Create an index, and fitness pair.
    return tournament(population, randomselections)


def tournament(population, selections):
    """
    Performs a single tournament.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        selections: (:obj:`list` of :obj:`Track`): The randomly selected tracks to return a fitness from.

    Returns:
        :obj:`Track`: The winning track from the tournament.
    """
    index = max(selections, key=itemgetter(1))[0]  # Return the index of the maximum fitness from a tuple.
    return population[index]
