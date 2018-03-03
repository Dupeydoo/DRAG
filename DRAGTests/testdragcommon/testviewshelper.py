from django import test
from DRAGProj.dragcommon import viewshelper as vh
from DRAGTests.mock.mockpopulation import MockPopulation
from DRAGProj.models.anonymoususer import AnonymousUser


class TestViewsHelper(test.TestCase):
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
        self.uuid = "HelloWorld"

    def test_gather_fitness_input(self):
        vh.gather_fitness_input(self.dict, self.population)
        values = [i[1] for i in self.dict]
        gathered = []
        for counter, track in enumerate(self.population):
            if track.fitness == values[counter]:
                gathered.append(True)
            else:
                gathered.append(False)

        self.assertEqual(False, False in gathered, "The fitnesses were not assigned correctly!")

    def test_generation_check(self):
        self.assertTrue(vh.generation_check(5, 5), "The given generations are not equal!")

    def test_create_user(self):
        vh.create_user(self.uuid)
        user = AnonymousUser.objects.get(UUID=self.uuid)
        self.assertEqual("HelloWorld", user.UUID, "The new user was not saved correctly!")

    def tearDown(self):
        del self.population, self.dict
