import unittest

from DRAGProj.geneticoperations import crossover
from DRAGTests.mock.mockpopulation import MockPopulation

"""
Test module for the crossover module from DRAGProj.

    Author:
        James

    Version:
        1.0.0
"""


class TestCrossover(unittest.TestCase):
    """
    Tests the crossover module.

    Attributes:
        parents (:obj:`MockPopulation`): A MockPopulation object for testing.
        cross_prob (float): The test probability of crossover.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.parents = MockPopulation()
        self.cross_prob = 1.0

    def test_do_crossover(self):
        """
        Tests the do_crossover function.
        """
        parents = self.parents.population
        children = crossover.do_crossover(parents, self.cross_prob)
        self.assertEqual(10, len(children), "Crossover did not succeed, elements were lost.")

    def test_single_point_crossover(self):
        """
        Tests the single_point_crossover function.
        """
        old_parents = [self.parents.population[0], self.parents.population[1]]
        parents = crossover.single_point_crossover(old_parents)
        self.assertNotEqual(parents[0], old_parents[0], "The tracks were not changed!")

    def test_multi_point_crossover(self):
        """
        Tests the multi_point_crossover function.
        """
        old_parents = [self.parents.population[0], self.parents.population[1]]
        parents = crossover.multi_point_crossover(old_parents)
        self.assertNotEqual(parents[1], old_parents[1], "The tracks were not changed!")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.parents, self.cross_prob
