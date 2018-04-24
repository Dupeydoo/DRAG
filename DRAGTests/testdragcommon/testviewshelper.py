from django import test

from DRAGProj.dragcommon import viewshelper as vh
from DRAGProj.models.anonymoususer import AnonymousUser
from DRAGTests.mock.mockpopulation import MockPopulation

"""
Test module for viewshelper module from DRAGProj.

    Author:
        James

    Version:
        2.0.0
"""


class TestViewsHelper(test.TestCase):
    """
    Tests the viewshelper module. Some methods are implicitly
    tested elsewhere.

    Attributes:
        population (:obj:`list` of :obj:`Track`): A population to test with.
        dict (:obj:`dict`): An example dictionary of fitness values at different
        beat positions.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
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
        """
        Tests the gather_fitness_input method.
        """
        vh.gather_fitness_input(self.dict, self.population)

        # Creates a list of dictionary values.
        values = [i[1] for i in self.dict]
        gathered = []
        for counter, track in enumerate(self.population):
            if track.fitness == values[counter]:
                gathered.append(True)
            else:
                gathered.append(False)

        self.assertEqual(False, False in gathered,
                         "The fitnesses were not assigned correctly!")

    def test_generation_check(self):
        """
        Tests the generation_check method.
        """
        self.assertTrue(vh.generation_check(5, 5),
                        "The given generations are not equal!")

    def test_create_user(self):
        """
        Tests the create_user method.
        """
        vh.create_user(self.uuid)
        user = AnonymousUser.objects.get(UUID=self.uuid)
        self.assertEqual("HelloWorld", user.UUID,
                         "The new user was not saved correctly!")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.population, self.dict
