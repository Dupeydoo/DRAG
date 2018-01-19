import random

from DRAGProj.dragcommon.track import Track

"""
The crossover module provides the crossover functions for the genetic algorithm.

    Author:
        James
        
    Version:
        3.2.0
        
    See:
        DRAGProj.dragcommon.track
        random
"""


def do_crossover(parents, cross_prob, single_point_prob=0.5):
    """
    The entry function to the crossover module.

    Args:
        parents (:obj:`list` of :obj:`Track`): The selected parents to crossover.
        cross_prob (float): The probability of crossover occurring.
        single_point_prob (float): Probability of single-point crossover occurring.

    Returns:
        children (:obj:`list` of :obj:`Track`): The children produced by crossover.
    """
    children = []
    for parent_one, parent_two in zip(*[iter(parents)] * 2):
        # For every pair in the parents iterable.
        pair = [parent_one, parent_two]
        if random.random() < cross_prob:  # Do we perform crossover.
            Track.pair_changed(pair)  # Update if the tracks have been modified.

            if random.random() < single_point_prob:
                children += single_point_crossover(pair)

            else:
                children += multi_point_crossover(pair)

        else:
            children += pair  # Otherwise just add them to the children.
    return children


def single_point_crossover(parents):
    """
    Performs single-point crossover.

    Args:
        parents (:obj:`list` of :obj:`Track`): The selected parents to crossover.

    Returns:
        children (:obj:`list` of :obj:`Track`): The children produced by crossover.
    """
    rand_index = random.randrange(0, len(parents[0].content))  # Choose a random crossover point.
    children = recombine(parents, rand_index)
    return children


def multi_point_crossover(parents):
    """
    Performs single-point crossover.

    Args:
        parents (:obj:`list` of :obj:`Track`): The selected parents to crossover.

    Returns:
        children (:obj:`list` of :obj:`Track`): The children produced by crossover.
    """
    first_index = random.randrange(0, len(parents[0].content))
    second_index = random.randrange(first_index, len(parents[0].content))  # Choose two random crossover points.
    children = multi_recombine(parents, first_index, second_index)
    return children


def recombine(parents, index):
    """
    Performs the actual single-point recombination. Makes use of python list slicing to build output
    tracks.

    Args:
        parents (:obj:`list` of :obj:`Track`): The selected parents to crossover.
        index (int): The index to crossover at.

    Returns:
        :obj:`list` of :obj:`Track`: The children produced by crossover.
    """
    first_parent = parents[0].content
    second_parent = parents[1].content
    # Slice up to and after the crossover points between the two lists.
    first_child = Track((first_parent[:index] + second_parent[index:]), parents[0].fitness, parents[0].track_id)
    second_child = Track((second_parent[:index] + first_parent[index:]), parents[1].fitness, parents[1].track_id)
    return [first_child, second_child]


def multi_recombine(parents, idx_one, idx_two):
    """
    Performs the actual multi-point recombination. Makes use of python list slicing to build output
    tracks.

    Args:
        parents (:obj:`list` of :obj:`Track`): The selected parents to crossover.
        idx_one (int): The first index to crossover at.
        idx_two (int): The second index to crossover at.

    Returns:
        :obj:`list` of :obj:`Track`: The children produced by crossover.
    """
    first_parent = parents[0].content
    second_parent = parents[1].content
    # List slices up to the first point, between the points, and after the last point.
    first_child = Track((first_parent[:idx_one] + second_parent[idx_one:idx_two] + first_parent[idx_two:]),
                        parents[0].fitness,
                        parents[0].track_id)

    second_child = Track((second_parent[:idx_one] + first_parent[idx_one:idx_two] + second_parent[idx_two:]),
                         parents[1].fitness,
                         parents[1].track_id)
    return [first_child, second_child]
