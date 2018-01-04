import random
import DRAGProj.mappers.drummapper as dm

from DRAGProj.dragcommon.track import Track

"""
The mutation module provdes the functions for mutation in the genetic algorithm.

    Author:
        James
        
    Version:
        2.1.0
"""


def domutation(children, mutaprob):
    """
    The entry function to mutation.

    Args:
        children (:obj:`list` of :obj:`Track`): The list of children from crossover.
        mutaprob (float): The probability of mutation occuring.

    Returns:
        mutatedchildren (:obj:`list` of :obj:`Track`): A list of children that have been mutated.
    """
    mutatedchildren = []
    for child in children:
        # If we perform mutation.
        if random.random() < mutaprob:
            child.hasChanged = True  # Some children may have not been changed by crossover.
            mutatedchildren.append(mutate(child))

        else:
            mutatedchildren.append(child)

    return mutatedchildren


def mutate(child):
    """
    Performs simple random drum choice mutation on a child.

    Args:
        child (:obj:`Track`): A child that will be mutated (sounds nasty).

    Returns:
        child (:obj:`Track`): A mutated child.
    """
    randindex = random.randrange(0, len(child.content))  # Pick an index to mutate.
    instruments = list(dm.drummapper.keys())  # Get the drum corresponding.
    child.content[randindex] = random.choice(instruments)  # Set the child's index to a new value.
    return child


def drumgroupmutate(child):
    """
    Performs a sophisticated random drum choice mutation on a child.
    based on different drum sounds, e.g. symbal or not symbal.

    Args:
        child (:obj:`Track`): A child that will be mutated (sounds nasty).

    Returns:
        child (:obj:`Track`): A mutated child.
    """
    instruments = dm.drummapper  # Get the possible instruments.
    randindex = random.randrange(0, len(child.content))
    groups = creategroups(instruments, child, randindex)
    if dm.isSymbal(groups[2]):  # If the random index is a symbal
        child.content[randindex] = random.choice(groups[0])  # Replace it with a symbal.
    else:
        child.content[randindex] = random.choice(groups[1])  # Or replace it with a drum if not.
    return child


def creategroups(instruments, child, randindex):
    """
    Picks a random drum and creates groups of symbal and non-symbals.

    Args:
        instruments (:obj:`dict` of int keys and :obj:`str` values): The instruments that can be used in DRAG.
        child (:obj:`Track`): A child that will be mutated.
        randindex (int): The index of the tracks contents to be mutated.
    """
    hihats = [d[0] for d in instruments.items() if "HHat" in d[1]]  # Comprehension: Output list is all symbals' keys.
    drums = [d[0] for d in instruments.items() if not "HHat" in d[1]]  # Comprehension: Output list is all drums' keys.
    childdrum = child.content[randindex]
    return hihats, drums, childdrum
