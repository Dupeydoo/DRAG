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

    def test_form(self):
        self.assertTrue(self.fitness_form.is_valid(), "The fitness form is invalid!")

    def test_form_data(self):
        self.fitness_form.is_valid()
        self.assertEqual(9, self.fitness_form.cleaned_data["fitness4"], "The form data is invalid!")

    def tearDown(self):
        del self.form_data, self.fitness_form
