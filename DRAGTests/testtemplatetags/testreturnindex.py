import unittest

"""
Test module for the returnindex module from DRAGProj.

    Author:
        James

    Version:
        1.0.0
"""


class TestReturnIndex(unittest.TestCase):
    """
    Tests the returnindex module.

    Attributes:
        content (:obj:`list` of int): A list of drums forming
        a single track.

        index (int): The index of a track to return a value at.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.content = [1, 2, 3, 4, 5, 6, 7, 8]
        self.index = 4

    def test_return_index(self):
        """
        Tests the return_index function.
        """
        def return_index(lst, index):
            """
            An identical copy of the return index
            function.
            """
            return lst[index]

        self.assertEqual(5, return_index(self.content, self.index),
                         "The index returned should have value 5!")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.content, self.index
