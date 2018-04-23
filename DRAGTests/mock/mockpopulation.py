from DRAGProj.dragcommon.track import Track

"""
Module to mock a single GA population as
a reusable object.

    Author:
        James
        
    Version:
        1.0.0
"""


class MockPopulation:
    """
    Mocks the population in a GA as a class to
    allow for fake populations in testing classes.

    Attributes:
        population (:obj:`list`): To be populated with tracks.
        child_population (:obj:`list`): A second list to be used
        for replacement testing where an old and new population
        are needed.
    """
    def __init__(self):
        """
        MockPopulation constructor. Populates the populations
        required.
        """
        self.population = []
        self.child_population = []
        self._populate()
        self._populate_child_population()

    def _populate(self):
        """
        Private method to populate the old population with
        sample tracks.
        """
        for i in range(10):
            self.population.append(Track([1, 2, 3, 4, 5, 6, 7, 8], 1))

    def _populate_child_population(self):
        """
        Private method to populate the new population with
        sample tracks.
        """
        for i in range(10):
            self.child_population.append(Track([8, 7, 6, 5, 4, 3, 2, 1], 1))
