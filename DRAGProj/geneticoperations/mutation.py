import random
import DRAGProj.mappers.drummapper as dm

"""
The mutation module provides the functions for mutation in the genetic algorithm.

    Author:
        James
        
    Version:
        2.1.0
"""


def do_mutation(children, muta_prob, muta_type_prob=0.5):
    """
    The entry function to mutation.

    Args:
        children (:obj:`list` of :obj:`Track`): The list of children from crossover.
        muta_prob (float): The probability of mutation occuring.

    Returns:
        mutated_children (:obj:`list` of :obj:`Track`): A list of children that have been mutated.
    """
    mutated_children = []
    for child in children:
        # If we perform mutation.
        if random.random() < muta_prob:
            child.has_changed = True  # Some children may have not been changed by crossover.
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
    rand_index = random.randrange(0, len(child.content))    # Pick an index to mutate.
    instruments = list(dm.drum_mapper.keys())               # Get the drum corresponding.
    instruments.remove(child.content[rand_index])           # Prevent choosing the same drum.
    child.content[rand_index] = random.choice(instruments)  # Set the child's index to a new value.
    return child


def drum_group_mutate(child):
    """
    Performs a sophisticated random drum choice mutation on a child.
    based on different drum sounds, e.g. symbal or not symbal.

    Args:
        child (:obj:`Track`): A child that will be mutated (sounds nasty).

    Returns:
        child (:obj:`Track`): A mutated child.
    """
    instruments = dm.drum_mapper                              # Get the possible instruments.
    rand_index = random.randrange(0, len(child.content))
    groups = create_groups(instruments, child, rand_index)

    if dm.is_cymbal(groups[2]):                               # If the random index is a cymbal
        child.content[rand_index] = random.choice(groups[0])  # Replace it with a cymbal.
    else:
        child.content[rand_index] = random.choice(groups[1])  # Or replace it with a drum if not.
    return child


def create_groups(instruments, child, rand_index):
    """
    Picks a random drum and creates groups of cymbal and non-cymbals.

    Args:
        instruments (:obj:`dict` of int keys and :obj:`str` values): The instruments that can be used in DRAG.
        child (:obj:`Track`): A child that will be mutated.
        rand_index (int): The index of the tracks contents to be mutated.
    """
    hi_hats = [d[0] for d in instruments.items() if "HHat" in d[1]]    # Comprehension: Output list is cymbals' keys.
    drums = [d[0] for d in instruments.items() if "HHat" not in d[1]]  # Comprehension: Output list is drums' keys.
    child_drum = child.content[rand_index]
    return hi_hats, drums, child_drum
