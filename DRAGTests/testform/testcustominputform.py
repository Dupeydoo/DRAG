from django.test import TestCase

from DRAGProj.forms.custominputform import CustomInputForm

"""
Test module for the CustomInputForm class from DRAGProj.

    Author:
        James

    Version:
        1.0.2
"""


class TestCustomInputForm(TestCase):
    """
    Tests the CustomInputForm class.

    Attributes:
        form_data (:obj:`dict`): Faked form data for testing.
        input_form (:obj:`CustomInputForm`): A form to test with.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.form_data = {
            "beat_one": 1,
            "beat_two": 2,
            "beat_three": 3,
            "beat_four": 4,
            "beat_five": 5,
            "beat_six": 6,
            "beat_seven": 7,
            "beat_eight": 8,
            "bpm": 150,
            "genre": "Rock"
        }
        self.input_form = CustomInputForm(data=self.form_data)

    def test_form(self):
        """
        Tests the CustomInputForm validity.
        """
        self.assertTrue(self.input_form.is_valid(), "The input_form data is invalid!")

    def test_form_data(self):
        """
        Tests for equality of CustomInputForm data.
        """
        self.input_form.is_valid()
        self.assertEqual(6, self.input_form.cleaned_data["beat_six"], "The form data has an incorrect value!")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.input_form, self.form_data
