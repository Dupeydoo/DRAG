import unittest
from DRAGProj.geneticoperations import generationalreplacement as gr
from DRAGTests.mock.mockpopulation import MockPopulation


class TestGenerationalReplacement(unittest.TestCase):
    def setUp(self):
        self.oldpopulation = MockPopulation().population
        self.newpopulation = MockPopulation().childpopulation

    def testdoreplacement(self):
        population = gr.doreplacement(self.oldpopulation, self.newpopulation)
        self.assertNotEqual(population[0].content, self.oldpopulation[0].content)

    def tearDown(self):
        del self.oldpopulation, self.newpopulation
