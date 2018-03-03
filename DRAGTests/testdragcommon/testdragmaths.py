import unittest
from DRAGProj.dragcommon.dragmaths import is_even


class TestDragMaths(unittest.TestCase):
    def setUp(self):
        self.number = 8

    def test_is_even(self):
        self.assertEqual(True, is_even(self.number),
                         "It should be True! 8 is an even number. "
                         "Expected: %r, Actual: % r" % (True, False))

    def tearDown(self):
        del self.number
