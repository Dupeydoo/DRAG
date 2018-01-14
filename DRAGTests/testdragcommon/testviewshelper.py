import unittest
from DRAGProj.dragcommon import viewshelper as vh
from DRAGTests.mock.mockpopulation import MockPopulation


class TestViewsHelper(unittest.TestCase):
    def setUp(self):
        self.population = MockPopulation().population
        self.dict = [
            ("one", 1),
            ("two", 2),
            ("three", 3),
            ("four", 4),
            ("five", 5),
            ("six", 6),
            ("seven", 7),
            ("eight", 8),
            ("nine", 9),
            ("ten", 10)
        ]

    def testgatherfitnessinput(self):
        vh.gatherfitnessinput(self.dict, self.population)
        values = [i[1] for i in self.dict]
        gathered = []
        for counter, track in enumerate(self.population):
            if track.fitness == values[counter]:
                gathered.append(True)
            else:
                gathered.append(False)

        self.assertEqual(False, False in gathered, "The fitnesses were not assigned correctly!")

    def tearDown(self):
        del self.population, self.dict
