import unittest
from DRAGProj.geneticoperations import selection
from DRAGTests.mock.mockpopulation import MockPopulation


class TestSelection(unittest.TestCase):
    def setUp(self):
        self.population = MockPopulation().population
        self.tournamentsize = 5

    def testdoselection(self):
        parents = selection.doselection(self.population, self.tournamentsize)
        changed = True if parents[0].hasChanged else False
        self.assertTrue(not changed, "The selected parents were't reset, or the parents weren't selected!")

    def testtournamentselect(self):
        parent = selection.tournamentselect(self.population, self.tournamentsize)
        self.assertEqual(1, parent.fitness, "The tournament was performed incorrectly!")

    def tearDown(self):
        del self.population, self.tournamentsize
