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


def docrossover(parents, crossprob, singlepointprob=0.5):
    """
    The entry function to the crossover module.

    Args:
        parents (:obj:`list` of :obj:`Track`): The selected parents to crossover.
        crossprob (float): The probability of crossover occuring.

    Returns:
        children (:obj:`list` of :obj:`Track`): The children produced by crossover.
    """
    children = []
    for parentone, parenttwo in zip(*[iter(parents)] * 2):
        # For every pair in the parents iterable.
        pair = [parentone, parenttwo]
        if random.random() < crossprob:  # Do we perform crossover.
            Track.pairchanged(pair)  # Update if the tracks have been modified.

            if random.random() < singlepointprob:
                children += singlepointcrossover(pair)

            else:
                children += multipointcrossover(pair)

        else:
            children += pair  # Otherwise just add them to the children.
    return children


def singlepointcrossover(parents):
    """
    Performs single-point crossover.

    Args:
        parents (:obj:`list` of :obj:`Track`): The selected parents to crossover.

    Returns:
        children (:obj:`list` of :obj:`Track`): The children produced by crossover.
    """
    randindex = random.randrange(0, len(parents[0].content))  # Choose a random crossover point.
    children = recombine(parents, randindex)
    return children


def multipointcrossover(parents):
    """
    Performs single-point crossover.

    Args:
        parents (:obj:`list` of :obj:`Track`): The selected parents to crossover.

    Returns:
        children (:obj:`list` of :obj:`Track`): The children produced by crossover.
    """
    firstindex = random.randrange(0, len(parents[0].content))
    secondindex = random.randrange(firstindex, len(parents[0].content))  # Choose two random crossover points.
    children = multirecombine(parents, firstindex, secondindex)
    return children


def recombine(parents, index):
    """
    Performs the actual single-point recombination. Makes use of python list slicing to build output
    tracks.

    Args:
        parents (:obj:`list` of :obj:`Track`): The selected parents to crossover.

    Returns:
        :obj:`list` of :obj:`Track`: The children produced by crossover.
    """
    firstparent = parents[0].content
    secondparent = parents[1].content
    # Slice up to and after the crossover points between the two lists.
    firstchild = Track((firstparent[:index] + secondparent[index:]), parents[0].fitness, parents[0].trackid)
    secondchild = Track((secondparent[:index] + firstparent[index:]), parents[1].fitness, parents[1].trackid)
    return [firstchild, secondchild]


def multirecombine(parents, idxone, idxtwo):
    """
    Performs the actual multi-point recombination. Makes use of python list slicing to build output
    tracks.

    Args:
        parents (:obj:`list` of :obj:`Track`): The selected parents to crossover.

    Returns:
        :obj:`list` of :obj:`Track`: The children produced by crossover.
    """
    firstparent = parents[0].content
    secondparent = parents[1].content
    # List slices up to the first point, between the points, and after the last point.
    firstchild = Track((firstparent[:idxone] + secondparent[idxone:idxtwo] + firstparent[idxtwo:]),
                       parents[0].fitness,
                       parents[0].trackid)

    secondchild = Track((secondparent[:idxone] + firstparent[idxone:idxtwo] + secondparent[idxtwo:]),
                        parents[1].fitness,
                        parents[1].trackid)
    return [firstchild, secondchild]
