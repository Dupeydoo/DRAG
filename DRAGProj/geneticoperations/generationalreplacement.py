"""
This module performs replacement of the population using a simple generational approach.

    Author:
        James

    Version:
        1.0.0
"""


def do_replacement(current_population, children):
    """
    Performs replacement.

    Args:
        current_population (:obj:`list` of :obj:`Track`): Current track population.
        children (:obj:`list` of :obj:`Track`): The children that will replace the old population.

    Returns:
        new_population (:obj:`list` of :obj:`Track`): New track population.
    """
    new_population = list(current_population)  # Assign a new memory reference.
    for candidate in range(len(new_population)):
        new_population[candidate] = children[candidate]
    return new_population
