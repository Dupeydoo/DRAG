import unittest

from DRAGProj.generators import genregenerator as gg

"""
Test module for the genregenerator module from DRAGProj.

    Author:
        James

    Version:
        1.4.0
"""


class TestGenreGenerator(unittest.TestCase):
    """
    Tests the genregenerator module.

    Attributes:
        structure (:obj:`list` of int): A structure to generate tracks with.
        time_sig (int): The time signature.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.structure = [1, 5, 6, 7, 8, 9, 10, 11]
        self.time_sig = 8

    def test_build_track_length(self):
        """
        Tests the build_track length results.
        """
        track = gg.build_track(self.structure, self.time_sig)
        correct_length = True if len(track.content) == 8 else False
        self.assertTrue(correct_length, "The track was not completed!")

    def test_build_track_structure(self):
        """
        Tests that the build_track function uses the structure.
        """
        track = gg.build_track(self.structure, self.time_sig)
        correct_members = True
        for drum in track.content:
            if drum not in self.structure:
                correct_members = False
        self.assertTrue(correct_members, "The track used unexpected drums!")

    def test_generate_tracks(self):
        """
        Tests the generation of tracks with generate_rock_tracks.
        """
        population = gg.generate_rock_tracks([], 5, 8)
        correct_length = True if len(population) == 5 else False
        self.assertTrue(correct_length,
                        "The population was created incorrectly!")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.structure, self.time_sig
