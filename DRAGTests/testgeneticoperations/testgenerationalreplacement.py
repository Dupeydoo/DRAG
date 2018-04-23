import unittest

from DRAGProj.geneticoperations import generationalreplacement as gr
from DRAGTests.mock.mockpopulation import MockPopulation

"""
Test module for the generationalreplacement module 
from DRAGProj.

    Author:
        James

    Version:
        1.0.0
"""


class TestGenerationalReplacement(unittest.TestCase):
    """
    Tests the generationalreplacement module.

    Attributes:
        old_population (:obj:`list` of :obj:`Track`): The old population to replace.
        new_population (:obj:`list` of :obj:`Track`): The new population.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.old_population = MockPopulation().population
        self.new_population = MockPopulation().child_population

    def test_do_replacement(self):
        """
        Tests the do_replacement function.
        """
        population = gr.do_replacement(self.old_population, self.new_population)
        self.assertNotEqual(population[0].content, self.old_population[0].content)

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.old_population, self.new_population
