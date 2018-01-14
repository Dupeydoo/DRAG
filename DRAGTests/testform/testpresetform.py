from django.test import TestCase
from DRAGProj.forms.presetform import PresetForm


class TestPresetForm(TestCase):
    def setUp(self):
        self.formdata = {
            "preset": 1,
            "bpm": 200
        }
        self.presetform = PresetForm(data=self.formdata)

    def testform(self):
        self.assertTrue(self.presetform.is_valid(), "The preset form is invalid!")

    def testformdata(self):
        self.presetform.is_valid()
        self.assertEqual(200, self.presetform.cleaned_data["bpm"], "The form data is invalid!")

    def tearDown(self):
        del self.formdata, self.presetform
