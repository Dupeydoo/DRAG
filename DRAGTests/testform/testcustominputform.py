from django.test import TestCase
from DRAGProj.forms.custominputform import CustomInputForm


class TestCustomInputForm(TestCase):
    def setUp(self):
        self.formdata = {
            "beatone": 1,
            "beattwo": 2,
            "beatthree": 3,
            "beatfour": 4,
            "beatfive": 5,
            "beatsix": 6,
            "beatseven": 7,
            "beateight": 8,
            "bpm": 150,
            "genre": "Rock"
        }
        self.inputform = CustomInputForm(data=self.formdata)

    def testform(self):
        self.assertTrue(self.inputform.is_valid(), "The inputform data is invalid!")

    def testformdata(self):
        self.inputform.is_valid()
        self.assertEqual(6, self.inputform.cleaned_data["beatsix"], "The form data has an incorrect value!")

    def tearDown(self):
        del self.inputform, self.formdata
