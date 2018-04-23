import unittest

from DRAGProj.geneticoperations import selection
from DRAGTests.mock.mockpopulation import MockPopulation

"""
Test module for the selection module from DRAGProj.

    Author:
        James

    Version:
        1.0.0
"""


class TestSelection(unittest.TestCase):
    """
    Tests the selection module.

    Attributes:
        population (:obj:`list` of :obj:`Track`): A testing population of tracks.
        tournament_size (int): The testing tournament size.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.population = MockPopulation().population
        self.tournament_size = 5

    def test_do_selection(self):
        """
        Tests the do_selection method.
        """
        parents = selection.do_selection(self.population, self.tournament_size)
        changed = True if parents[0].has_changed else False
        self.assertTrue(not changed, "The selected parents were't reset, or the parents weren't selected!")

    def test_tournament_select(self):
        """
        Tests the tournament_select function.
        """
        parent = selection.tournament_select(self.population, self.tournament_size)
        self.assertEqual(1, parent.fitness,
                         "The tournament was performed incorrectly! Actual: %d, Expected: %d" % (parent.fitness, 1))

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.population, self.tournament_size
