from django.test import TestCase

from DRAGProj.forms.presetform import PresetForm

"""
Test module for the PresetForm class from DRAGProj.

    Author:
        James

    Version:
        1.0.0
"""


class TestPresetForm(TestCase):
    """
    Tests the PresetForm class.

    Attributes:
        form_data (:obj:`dict`): Faked form data for testing.
        preset_form (:obj:`PresetForm`): A form to test with.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.form_data = {
            "preset": 1,
            "bpm": 200
        }
        self.preset_form = PresetForm(data=self.form_data)

    def test_form(self):
        """
        Tests the Preset form validity.
        """
        self.assertTrue(self.preset_form.is_valid(), "The preset form is invalid!")

    def test_form_data(self):
        """
        Tests for equality of Preset form data.
        """
        self.preset_form.is_valid()
        self.assertEqual(200, self.preset_form.cleaned_data["bpm"], "The form data is invalid!")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.form_data, self.preset_form
