from django.test import TestCase
from DRAGProj.forms.fitnessform import FitnessForm


class TestFitnessForm(TestCase):
    def setUp(self):
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
        self.assertTrue(self.fitness_form.is_valid(), "The fitness form is invalid!")

    def test_form_data(self):
        self.fitness_form.is_valid()
        self.assertEqual(9, self.fitness_form.cleaned_data["fitness4"], "The form data is invalid!")

    def test_collect_fitnesses(self):
        tuple_dict = self.fitness_form.collect_fitnesses()
        output = []
        for pair in tuple_dict:
            output.append(pair[1])
        self.assertEqual([5, 2, 9, 0, 3], output, "Fitnesses were not collated correctly.")

    def tearDown(self):
        del self.form_data, self.fitness_form
