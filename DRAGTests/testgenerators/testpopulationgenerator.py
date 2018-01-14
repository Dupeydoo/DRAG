import unittest
from DRAGProj.generators import populationgenerator as pg
from DRAGTests.mock.mockpopulation import MockPopulation


class TestPopulationGenerator(unittest.TestCase):
    def setUp(self):
        self.population = []
        self.psize = 10
        self.copynumber = 4
        self.inputlist = [8, 7, 6, 5, 4, 3, 2, 1]
        self.genre = "Rock"
        self.timesig = 8

    def testgeneratepopulation(self):
        self.population = pg.generatepopulation(self.psize, 0.4, self.inputlist, self.genre, self.timesig)
        correctpopulation = True if len(self.population) == 10 else False
        self.assertTrue(correctpopulation, "The population has not been built as expected!")

    def testpopulatecopieslength(self):
        self.population = pg.populatecopies(self.population, self.copynumber, self.inputlist)
        correctcopies = True if len(self.population) == 4 else False
        self.assertTrue(correctcopies, "The amount of copies is incorrect!")

    def testpopulatecopiescontent(self):
        self.population = pg.populatecopies(self.population, self.copynumber, self.inputlist)
        elementmatch = []
        for counter, pop in enumerate(self.population[0].content):
            if pop == self.inputlist[counter]:
                elementmatch.append(True)
            else:
                elementmatch.append(False)

        self.assertTrue(not False in elementmatch, "The elements of the copies don't match the inputlist!")

    def tearDown(self):
        del self.population, self.psize, self.copynumber, self.inputlist, self.genre, self.timesig
