from django.test import TestCase

from DRAG.datacontext import context
from DRAGProj.dragcommon import formhelper as fh
from DRAGProj.models.preset import Preset

"""
Test module for the formhelper module from DRAGProj.

    Author:
        James

    Version:
        1.1.1
"""


class TestFormHelper(TestCase):
    """
    Class to test the formhelper module.

    Attributes:
        clean (:obj:`dict`): A fake cleaned form dictionary.
        context (:obj:`dict`): The dictionary of algorithm parameters.
        preset (:obj:`Preset`): A Preset object.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.clean = {
            "beat_one": 1,
            "beat_two": 1,
            "beat_three": 1,
            "beat_four": 1,
            "beat_five": 1,
            "beat_six": 1,
            "beat_seven": 1,
            "beat_eight": 1
        }
        self.context = context
        self.preset = Preset()
        self.preset.beat_one = 2
        self.preset.beat_two = 1
        self.preset.beat_three = 3
        self.preset.beat_four = 1
        self.preset.beat_five = 2
        self.preset.beat_six = 1
        self.preset.beat_seven = 3
        self.preset.beat_eight = 1
        self.preset.save()

    def test_construct_input(self):
        """
        Tests the construct_input method.
        """
        self.assertEqual([1, 1, 1, 1, 1, 1, 1, 1],
                         fh.construct_input(self.clean),
                         "The input should be [1,1,1,1,1,1,1,1]")

    def test_get_preset(self):
        """
        Tests the get_preset method.
        """
        self.assertEqual([2, 1, 3, 1, 2, 1, 3, 1], fh.get_preset(0),
                         "Preset should be [2, 1, 3, 1, 2, 1, 3, 1]")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.clean, self.context
