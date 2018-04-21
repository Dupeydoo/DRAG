from django.test import TestCase
from DRAGNN.machinelearning import classification as cl

"""
Most of the methods presented in classification are chained,
thus, they will be tested in full in integration tests rather
than this unit test class.
"""


class TestClassification(TestCase):
    def setUp(self):
        self.fitnesses = [1, 9, 0, 4, 6, 5, 8, 3, 2, 8]

    def test_decompose_fitness(self):
        expected_output = [0, 2, 0, 1, 1, 1, 2, 0, 0, 2]
        self.assertEquals(expected_output, cl.decompose_fitness(self.fitnesses),
                          "The classes were decomposed incorrectly!")

    def tearDown(self):
        del self.fitnesses
