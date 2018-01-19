import unittest
from DRAGProj.dragcommon.dragmaths import is_even


class TestDragMaths(unittest.TestCase):
    def test_is_even(self):
        self.assertEqual(True, is_even(8), "It should be True! 8 is an even number.")
