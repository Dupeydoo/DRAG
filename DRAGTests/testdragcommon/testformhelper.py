from django.test import TestCase
from DRAG.datacontext import context
from DRAGProj.dragcommon import formhelper as fh
from DRAGProj.models.preset import Preset


class TestFormHelper(TestCase):
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
        self.preset = Preset()
        self.preset.beat_one = 2
        self.preset.beat_two = 1
        self.preset.beat_three = 3
        self.preset.beat_four = 1
        self.preset.beat_five = 2
        self.preset.beat_six = 1
        self.preset.beat_seven = 3
        self.preset.beat_eight = 1
        self.preset.save()

    def test_construct_input(self):
        self.assertEqual([1, 1, 1, 1, 1, 1, 1, 1], fh.construct_input(self.clean),
                         "The input should be [1,1,1,1,1,1,1,1]")

    def test_get_preset(self):
        self.assertEqual([2, 1, 3, 1, 2, 1, 3, 1], fh.get_preset(0), "Preset should be [2, 1, 3, 1, 2, 1, 3, 1]")

    def tearDown(self):
        del self.clean, self.context
