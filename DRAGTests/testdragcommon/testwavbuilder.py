import unittest
from DRAGProj.dragcommon import wavbuilder as wb
from DRAG import datacontext as dc
import os


class TestWavBuilder(unittest.TestCase):
    def setUp(self):
        context = dc.context
        self.context = context
        self.wav_path = context["system_path"] + context["wav_path"]
        self.path = self.wav_path + "test.wav"
        self.bpm = 200

        with open(context["system_path"] + "/DRAGTests/testdragcommon/"
                  + "/testwavbuilder_clearwavcandidates/test.wav", "w") as file:
            file.write("Hello World.")

    def test_open_wav(self):
        file = wb.open_wav(self.path)
        self.assertEqual(1.0, file.duration_seconds, "Test.wav was not opened correctly!")

    def test_beat_offset(self):
        self.assertEqual(300, wb.beat_offset(200), "The beat offset was calculated incorrectly!")

    def test_clear_wav_candidates(self):
        wav_directory = self.context["system_path"] + "/DRAGTests/testdragcommon/" + \
                        "/testwavbuilder_clearwavcandidates/"
        wb.clear_wav_candidates(wav_directory, "test")
        self.assertEqual([], os.listdir(wav_directory), "Test.wav was not removed!")

    def tearDown(self):
        del self.wav_path, self.path, self.bpm
