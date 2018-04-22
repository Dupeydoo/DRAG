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
        # Perform tournament selection.
        parent = tournament_select(population, tournament_size)

        # Nullify changes from last generation.
        parent.has_changed = False
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
        rand_index = random.randrange(0, len(population))

        # Create an index, and fitness pair.
        random_selections.append((rand_index, population[rand_index].fitness))
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
    maximums = []

    # Find the first tuple with a maximum value.
    max_tuple = max(selections, key=itemgetter(1))
    for selection in range(len(selections)):
        sel = selections[selection]

        # Find matching maximum value tuples.
        if sel[1] == max_tuple[1]:
            maximums.append(selection)

    # If there are several matching maximum values
    # return a choice from them.
    maximum = random.choice(maximums)
    index = selections[maximum]
    return population[index[0]]


if __name__ == "__main__":
    from DRAGTests.mock.mockpopulation import MockPopulation

    mock = MockPopulation().population
    track = tournament_select(mock, 5)
    print(track.content)
