import unittest
from DRAG.datacontext import context
from DRAGProj.dragcommon import formhelper as fh


class TestFormHelper(unittest.TestCase):
    def setUp(self):
        self.clean = {
            "beatone": 1,
            "beattwo": 1,
            "beatthree": 1,
            "beatfour": 1,
            "beatfive": 1,
            "beatsix": 1,
            "beatseven": 1,
            "beateight": 1
        }
        self.context = context

    def testconstructinput(self):
        self.assertEqual([1, 1, 1, 1, 1, 1, 1, 1], fh.constructinput(self.clean),
                         "The input should be [1,1,1,1,1,1,1,1]")

    def testgetpreset(self):
        self.assertEqual([7, 7, 11, 1, 1, 11, 1, 1], fh.getpreset(1), "Preset should be [7,7,11,1,1,11,1,1]")

    def tearDown(self):
        del self.clean, self.context
