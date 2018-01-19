import unittest
from DRAGProj.geneticoperations import selection
from DRAGTests.mock.mockpopulation import MockPopulation


class TestSelection(unittest.TestCase):
    def setUp(self):
        self.population = MockPopulation().population
        self.tournament_size = 5

    def test_do_selection(self):
        parents = selection.do_selection(self.population, self.tournament_size)
        changed = True if parents[0].has_changed else False
        self.assertTrue(not changed, "The selected parents were't reset, or the parents weren't selected!")

    def test_tournament_select(self):
        parent = selection.tournament_select(self.population, self.tournament_size)
        self.assertEqual(1, parent.fitness, "The tournament was performed incorrectly!")

    def tearDown(self):
        del self.population, self.tournament_size
