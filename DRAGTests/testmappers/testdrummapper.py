import unittest
from DRAGProj.mappers import drummapper as dm


class TestDrumMapper(unittest.TestCase):
    def setUp(self):
        self.drum = 1

    def test_drum_mapper(self):
        self.assertEquals("HTomSnare.wav", dm.drum_mapper.get(10),
                          "The corresponding drum is wrong or has been changed!")

    def test_is_cymbal(self):
        self.assertTrue(dm.is_cymbal(self.drum), "Drum 1 is a Hi-Hat! is_cymbal should return true!")

    def tearDown(self):
        del self.drum
