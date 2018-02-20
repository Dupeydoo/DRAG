import random
from operator import itemgetter

"""
The selection module performs tournament selection for the genetic algorithm.

    Author:
        James
        
    Version:
        2.0.0
"""


def do_selection(population, tournament_size):
    """
    Entry point function for selection.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        tournament_size (int): Tournament size parameter used to control selection.

    Returns:
        parents (:obj:`list` of :obj:`Track`): The new population of tracks selected from the old.
    """
    parents = []
    for selections in range(len(population)):
        parent = tournament_select(population, tournament_size)  # Perform tournament selection.
        parent.has_changed = False                               # Nullify changes from last generation.
        parents.append(parent)
    return parents


def tournament_select(population, tournament_size):
    """
    Performs tournament selection.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        tournament_size (int): Tournament size parameter used to control selection.

    Returns:
        :obj:`Track`: A track that has been selected from a tournament.
    """
    random_selections = []
    for candidates in range(tournament_size):
        rand_index = random.randrange(0, len(population))                       # Pick a random index
        random_selections.append((rand_index, population[rand_index].fitness))  # Create an index, and fitness pair.
    return tournament(population, random_selections)


def tournament(population, selections):
    """
    Performs a single tournament.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        selections: (:obj:`list` of :obj:`Track`): The randomly selected tracks to return a fitness from.

    Returns:
        :obj:`Track`: The winning track from the tournament.
    """
    # TODO Don't just select the first max, choose a random max.
    index = max(selections, key=itemgetter(1))[0]  # Return the index of the maximum fitness from a tuple.
    return population[index]
