import random

import DRAGProj.mappers.drummapper as dm

"""
The mutation module provides the functions for mutation in the genetic 
algorithm.

    Author:
        James
        
    Version:
        2.1.0
"""


def do_mutation(children, muta_prob, muta_type_prob=0.5):
    """
    The entry function to mutation.

    Args:
        children (:obj:`list` of :obj:`Track`): The list of children from
        crossover.

        muta_prob (float): The probability of mutation occuring.
        muta_type_prob (float): Probability deciding whether to use single
        or multi-point crossover.

    Returns:
        mutated_children (:obj:`list` of :obj:`Track`): A list of children
        that have been mutated.
    """
    mutated_children = []
    for child in children:

        # If we perform mutation.
        if random.random() < muta_prob:

            # Some children may have not been changed by crossover.
            child.has_changed = True
            if random.random() < muta_type_prob:
                mutated_children.append(mutate(child))

            else:
                mutated_children.append(drum_group_mutate(child))
        else:
            mutated_children.append(child)

    return mutated_children


def mutate(child):
    """
    Performs simple random drum choice mutation on a child.

    Args:
        child (:obj:`Track`): A child that will be mutated (sounds nasty).

    Returns:
        child (:obj:`Track`): A mutated child.
    """
    # Pick an index to mutate.
    rand_index = random.randrange(0, len(child.content))

    # Get the corresponding drum.
    instruments = list(dm.drum_mapper.keys())

    # Prevent choosing the same drum.
    instruments.remove(child.content[rand_index])

    # Set the child's index to a new value.
    child.content[rand_index] = random.choice(instruments)
    return child


def drum_group_mutate(child):
    """
    Performs a sophisticated random drum choice mutation on a child.
    based on different drum sounds, e.g. cymbal or not cymbal.

    Args:
        child (:obj:`Track`): A child that will be mutated (sounds nasty).

    Returns:
        child (:obj:`Track`): A mutated child.
    """
    # Get the possible instruments.
    instruments = dm.drum_mapper
    rand_index = random.randrange(0, len(child.content))
    groups = create_groups(instruments, child, rand_index)

    # If the random index is a cymbal
    if dm.is_cymbal(groups[2]):
        # Replace it with a cymbal.
        child.content[rand_index] = random.choice(groups[0])
    else:
        # Or replace it with a drum if not.
        child.content[rand_index] = random.choice(groups[1])
    return child


def create_groups(instruments, child, rand_index):
    """
    Picks a random drum and creates groups of cymbal and non-cymbals.

    Args:
        instruments (:obj:`dict` of int keys and :obj:`str` values): The
        instruments that can be used in DRAG.

        child (:obj:`Track`): A child that will be mutated.
        rand_index (int): The index of the tracks contents to be mutated.
    """
    # Comprehension: Output list is cymbals' keys.
    hi_hats = [d[0] for d in instruments.items() if "HHat" in d[1]]

    # Comprehension: Output list is drums' keys.
    drums = [d[0] for d in instruments.items() if "HHat" not in d[1]]
    child_drum = child.content[rand_index]
    return hi_hats, drums, child_drum
