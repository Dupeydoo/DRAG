import unittest

"""
Test module for the strconcat module from DRAGProj.

    Author:
        James

    Version:
        1.0.0
"""


class TestStrConcat(unittest.TestCase):
    """
    Tests the strconcat module.

    Attributes:
        string_one (:obj:`str`): The first string to concatenate.
        string_two (:obj:`str`): The second string to concatenate.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.string_one = "Hello "
        self.string_two = "World!"

    def test_str_concat(self):
        """
        Tests the str_concat method.
        """
        def str_concat(string, another_string):
            return str(string) + str(another_string)

        self.assertEqual("Hello World!", str_concat(self.string_one, self.string_two))

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.string_one, self.string_two
