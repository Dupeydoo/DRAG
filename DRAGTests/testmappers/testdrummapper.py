import unittest

from DRAGProj.mappers import drummapper as dm

"""
Test module for the drummapper module from DRAGProj.

    Author:
        James

    Version:
        1.0.0
"""


class TestDrumMapper(unittest.TestCase):
    """
    Tests the drummapper module.

    Attributes:
        drum (int): A number representing a single drum to
        test initialisation of the drummapper dictionary.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.drum = 1

    def test_drum_mapper(self):
        """
        Tests the drummapper dictionary.
        """
        self.assertEquals("HTomSnare.wav", dm.drum_mapper.get(10),
                          "The corresponding drum is wrong or has been changed!")

    def test_is_cymbal(self):
        """
        Tests the is_cymbal method.
        """
        self.assertTrue(dm.is_cymbal(self.drum), "Drum 1 is a Hi-Hat! is_cymbal should return true!")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.drum
