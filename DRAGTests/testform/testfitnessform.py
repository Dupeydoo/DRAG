from django.test import TestCase
from DRAGProj.forms.fitnessform import FitnessForm


class TestFitnessForm(TestCase):
    def setUp(self):
        self.formdata = {
            "fitness0": 5,
            "fitness1": 8,
            "fitness2": 2,
            "fitness3": 3,
            "fitness4": 9
        }
        self.fitnessform = FitnessForm(size=5, data=self.formdata)

    def testform(self):
        self.assertTrue(self.fitnessform.is_valid(), "The fitness form is invalid!")

    def testformdata(self):
        self.fitnessform.is_valid()
        self.assertEqual(9, self.fitnessform.cleaned_data["fitness4"], "The form data is invalid!")

    def tearDown(self):
        del self.formdata, self.fitnessform
