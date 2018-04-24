from django.test import TestCase

from DRAGProj.forms.fitnessform import FitnessForm

"""
Test module for the FitnessForm class from DRAGProj.

    Author:
        James

    Version:
        1.0.0
"""


class TestFitnessForm(TestCase):
    """
    Tests the FitnessForm class.

    Attributes:
        form_data (:obj:`dict`): Faked form data for testing.
        fitness_form (:obj:`FitnessForm`): A form to test with.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.form_data = {
            "fitness0": 5,
            "fitness1": 8,
            "fitness2": 2,
            "fitness3": 3,
            "fitness4": 9
        }
        self.fitness_form = FitnessForm(size=5, data=self.form_data)
        self.fitness_form.cleaned_data = {
            "fitness0": 5,
            "fitness1": 2,
            "fitness2": 9,
            "fitness3": 0,
            "fitness4": 3,
        }

    def test_form(self):
        """
        Tests the FitnessForm validity.
        """
        self.assertTrue(self.fitness_form.is_valid(),
                        "The fitness form is invalid!")

    def test_form_data(self):
        """
        Tests for equality of FitnessForm data.
        """
        self.fitness_form.is_valid()
        self.assertEqual(9, self.fitness_form.cleaned_data["fitness4"],
                         "The form data is invalid!")

    def test_collect_fitnesses(self):
        """
        Tests the collect_fitnesses method.
        """
        tuple_dict = self.fitness_form.collect_fitnesses()
        output = []
        for pair in tuple_dict:
            output.append(pair[1])
        self.assertEqual([5, 2, 9, 0, 3], output,
                         "Fitnesses were not collated correctly.")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.form_data, self.fitness_form
