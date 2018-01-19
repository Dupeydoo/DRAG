import unittest
from DRAG.datacontext import context
from DRAGProj.dragcommon import formhelper as fh


class TestFormHelper(unittest.TestCase):
    def setUp(self):
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

    def test_construct_input(self):
        self.assertEqual([1, 1, 1, 1, 1, 1, 1, 1], fh.construct_input(self.clean),
                         "The input should be [1,1,1,1,1,1,1,1]")

    def test_get_preset(self):
        self.assertEqual([7, 7, 11, 1, 1, 11, 1, 1], fh.get_preset(1), "Preset should be [7,7,11,1,1,11,1,1]")

    def tearDown(self):
        del self.clean, self.context
