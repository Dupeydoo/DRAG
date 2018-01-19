import unittest
from DRAGProj.geneticoperations import generationalreplacement as gr
from DRAGTests.mock.mockpopulation import MockPopulation


class TestGenerationalReplacement(unittest.TestCase):
    def setUp(self):
        self.old_population = MockPopulation().population
        self.new_population = MockPopulation().child_population

    def test_do_replacement(self):
        population = gr.do_replacement(self.old_population, self.new_population)
        self.assertNotEqual(population[0].content, self.old_population[0].content)

    def tearDown(self):
        del self.old_population, self.new_population
