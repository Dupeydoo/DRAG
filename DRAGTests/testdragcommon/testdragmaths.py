import unittest
from DRAGProj.dragcommon.dragmaths import iseven


class TestDragMaths(unittest.TestCase):
    def testiseven(self):
        self.assertEqual(True, iseven(8), "It should be True! 8 is an even number.")
