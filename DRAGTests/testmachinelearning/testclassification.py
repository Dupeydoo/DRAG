from django.test import TestCase

from DRAGNN.machinelearning import classification as cl

"""
Test module for the classification module from DRAGProj.
Most classification methods were integrity tested over
unit testing due to their length of running exceeding
acceptable unit test length.

    Author:
        James
    
    Version:
        1.0.0
"""


class TestClassification(TestCase):
    """
    Tests the classification module.

    Attributes:
        fitnesses (:obj:`list` of int): A list of fitnesses to decompose.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.fitnesses = [1, 9, 0, 4, 6, 5, 8, 3, 2, 8]

    def test_decompose_fitness(self):
        """
        Tests the decompose_fitness method.
        """
        expected_output = [0, 2, 0, 1, 1, 1, 2, 0, 0, 2]
        self.assertEquals(expected_output, cl.decompose_fitness(self.fitnesses),
                          "The classes were decomposed incorrectly!")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.fitnesses
