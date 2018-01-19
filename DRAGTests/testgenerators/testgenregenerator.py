import unittest
from DRAGProj.generators import genregenerator as gg


class TestGenreGenerator(unittest.TestCase):
    def setUp(self):
        self.structure = [1, 5, 6, 7, 8, 9, 10, 11]
        self.time_sig = 8
        self.index = 3
        self.common_value = 7

    def test_build_track_length(self):
        track = gg.build_track(self.structure, self.time_sig, self.index, self.common_value)
        correct_length = True if len(track.content) == 8 else False
        self.assertTrue(correct_length)

    def test_build_track_common(self):
        track = gg.build_track(self.structure, self.time_sig, self.index, self.common_value)
        correct_value = True if track.content[self.index] == self.common_value else False
        self.assertTrue(correct_value)

    def test_generate_tracks(self):
        population = gg.generate_rock_tracks([], 5, 8)
        correct_length = True if len(population) == 5 else False
        self.assertTrue(correct_length)

    def tearDown(self):
        del self.structure, self.time_sig, self.index, self.common_value
