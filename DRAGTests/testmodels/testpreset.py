from django.test import TestCase

from DRAGProj.models.preset import Preset

"""
Test module for the Preset class from DRAGProj.

    Author:
        James

    Version:
        1.0.0
"""


class TestPreset(TestCase):
    """
    Tests the Preset class.

    Attributes:
        preset (:obj:`Preset`): A preset model to test with.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.preset = Preset()

    def test_preset(self):
        """
        Tests the preset constructor.
        """
        instance = True if isinstance(self.preset, Preset) else False
        self.assertTrue(instance, "The preset should be an instance "
                                  "of the Preset model class")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.preset
