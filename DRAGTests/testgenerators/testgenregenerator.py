import unittest
from DRAGProj.generators import genregenerator as gg


class TestGenreGenerator(unittest.TestCase):
    def setUp(self):
        self.structure = [1, 5, 6, 7, 8, 9, 10, 11]
        self.time_sig = 8

    def test_build_track_length(self):
        track = gg.build_track(self.structure, self.time_sig)
        correct_length = True if len(track.content) == 8 else False
        self.assertTrue(correct_length, "The track was not completed!")

    def test_build_track_structure(self):
        track = gg.build_track(self.structure, self.time_sig)
        correct_members = True
        for drum in track.content:
            if drum not in self.structure:
                correct_members = False
        self.assertTrue(correct_members, "The track used unexpected drums!")

    def test_generate_tracks(self):
        population = gg.generate_rock_tracks([], 5, 8)
        correct_length = True if len(population) == 5 else False
        self.assertTrue(correct_length, "The population was created incorrectly!")

    def tearDown(self):
        del self.structure, self.time_sig
