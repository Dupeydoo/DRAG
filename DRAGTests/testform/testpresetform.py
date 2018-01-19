from django.test import TestCase
from DRAGProj.forms.presetform import PresetForm


class TestPresetForm(TestCase):
    def setUp(self):
        self.form_data = {
            "preset": 1,
            "bpm": 200
        }
        self.preset_form = PresetForm(data=self.form_data)

    def test_form(self):
        self.assertTrue(self.preset_form.is_valid(), "The preset form is invalid!")

    def test_form_data(self):
        self.preset_form.is_valid()
        self.assertEqual(200, self.preset_form.cleaned_data["bpm"], "The form data is invalid!")

    def tearDown(self):
        del self.form_data, self.preset_form
