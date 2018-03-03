import unittest
from DRAGProj.geneticoperations import crossover
from DRAGTests.mock.mockpopulation import MockPopulation


class TestCrossover(unittest.TestCase):
    def setUp(self):
        self.parents = MockPopulation()
        self.cross_prob = 1.0

    def test_do_crossover(self):
        parents = self.parents.population
        children = crossover.do_crossover(parents, self.cross_prob)
        self.assertEqual(10, len(children), "Crossover did not succeed, elements were lost.")

    def test_single_point_crossover(self):
        old_parents = [self.parents.population[0], self.parents.population[1]]
        parents = crossover.single_point_crossover(old_parents)
        self.assertNotEqual(parents[0], old_parents[0], "The tracks were not changed!")

    def test_multi_point_crossover(self):
        old_parents = [self.parents.population[0], self.parents.population[1]]
        parents = crossover.multi_point_crossover(old_parents)
        self.assertNotEqual(parents[1], old_parents[1], "The tracks were not changed!")

    def tearDown(self):
        del self.parents, self.cross_prob
