from django.test import TestCase
from DRAGProj.models.preset import Preset


class TestPreset(TestCase):
    def setUp(self):
        self.preset = Preset()

    def test_preset(self):
        instance = True if isinstance(self.preset, Preset) else False
        self.assertTrue(instance, "The preset should be an instance of the Preset model class")

    def tearDown(self):
        del self.preset
