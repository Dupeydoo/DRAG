"""
This module performs replacement of the population using a simple generational approach.

    Author:
        James

    Version:
        1.0.0
"""

def doreplacement(currentpopulation, children):
    """
    Performs replacement.

    Args:
        currentpopulation (:obj:`list` of :obj:`Track`): Current track population.
        children (:obj:`list` of :obj:`Track`): The children that will replace the old population.

    Returns:
        newpopulation (:obj:`list` of :obj:`Track`): New track population.
    """
    newpopulation = list(currentpopulation)  # Assign a new memory reference.
    for candidate in range(len(newpopulation)):
        newpopulation[candidate] = children[candidate]
    return newpopulation



