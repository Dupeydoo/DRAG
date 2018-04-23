import os
import unittest

from DRAG import datacontext as dc
from DRAGProj.dragcommon import wavbuilder as wb

"""
Test module for the wavbuilder from DRAGProj.

    Author:
        James

    Version:
        1.0.0
"""


class TestWavBuilder(unittest.TestCase):
    """
    Tests the wavbuilder module.

    Attributes:
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        context = dc.context
        self.context = context
        self.wav_path = context["system_path"] + context["wav_path"]
        self.path = self.wav_path + "test.wav"
        self.bpm = 200

        # Write a new wav file for use in testing.
        with open(context["system_path"] + "/DRAGTests/testdragcommon/"
                  + "/testwavbuilder_clearwavcandidates/test.wav", "w") as file:
            file.write("Hello World.")

    def test_open_wav(self):
        """
        Tests the open_wav method.
        """
        file = wb.open_wav(self.path)
        self.assertEqual(1.0, file.duration_seconds, "Test.wav was not opened correctly!")

    def test_beat_offset(self):
        """
        Tests the beat_offset method.
        """
        self.assertEqual(300, wb.beat_offset(200), "The beat offset was calculated incorrectly!")

    def test_clear_wav_candidates(self):
        """
        Tests the clear_wav_candidates method.
        """
        wav_directory = self.context["system_path"] + "/DRAGTests/testdragcommon/" + \
                        "/testwavbuilder_clearwavcandidates/"
        wb.clear_wav_candidates(wav_directory, "test")
        self.assertEqual([], os.listdir(wav_directory), "Test.wav was not removed!")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.wav_path, self.path, self.bpm, self.context
