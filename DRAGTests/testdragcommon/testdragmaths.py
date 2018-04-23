import unittest

from DRAGProj.dragcommon.dragmaths import is_even

"""
Test module for the dragmaths module from DRAGProj.

    Author:
        James

    Version:
        1.0.0
"""


class TestDragMaths(unittest.TestCase):
    """
    Tests the dragmaths module.

    Attributes:
        number (int): A number to test to use for testing.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.number = 8

    def test_is_even(self):
        """
        Tests the is_even method.
        """
        self.assertEqual(True, is_even(self.number),
                         "It should be True! 8 is an even number. "
                         "Expected: %r, Actual: % r" % (True, False))

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.number
