import unittest

from DRAGProj.generators import populationgenerator as pg

"""
Test module for the populationgenerator from DRAGProj.

    Author:
        James

    Version:
        1.1.0
"""


class TestPopulationGenerator(unittest.TestCase):
    """
    Tests the populationgenerator module.

    Attributes:
        population (:obj:`list`): An empty population.
        p_size (int): The population size to generate.
        copy_number (int): The number of copies to generate.
        input_list (:obj:`list` of int): The input list to copy.
        genre (:obj:`str`): The genre to generate (always rock in prod).
        time_sig (int): The time signature.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.population = []
        self.p_size = 10
        self.copy_number = 4
        self.input_list = [8, 7, 6, 5, 4, 3, 2, 1]
        self.genre = "Rock"
        self.time_sig = 8

    def test_generate_population(self):
        """
        Tests the generate_population function.
        """
        self.population = pg.generate_population(self.p_size, 0.4, self.input_list, self.genre, self.time_sig)
        correct_population = True if len(self.population) == 10 else False
        self.assertTrue(correct_population, "The population has not been built as expected!")

    def test_populate_copies_length(self):
        """
        Tests the populate_copies function for length results.
        """
        self.population = pg.populate_copies(self.population, self.copy_number, self.input_list)
        correct_copies = True if len(self.population) == 4 else False
        self.assertTrue(correct_copies, "The amount of copies is incorrect!")

    def test_populate_copies_content(self):
        """
        Tests the populate_copies function for content results.
        """
        self.population = pg.populate_copies(self.population, self.copy_number, self.input_list)
        element_match = []
        for counter, pop in enumerate(self.population[0].content):
            if pop == self.input_list[counter]:
                element_match.append(True)
            else:
                element_match.append(False)

        self.assertTrue(not False in element_match, "The elements of the copies don't match the input_list!")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.population, self.p_size, self.copy_number, self.input_list, self.genre, self.time_sig
