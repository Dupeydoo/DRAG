import unittest
from DRAGProj.dragcommon import wavbuilder as wb
from DRAG import datacontext as dc


class TestWavBuilder(unittest.TestCase):
    def setUp(self):
        context = dc.context
        self.wav_path = context["systempath"] + context["wavpath"]
        self.path = self.wav_path + "test.wav"
        self.bpm = 200

    def test_open_wav(self):
        file = wb.open_wav(self.path)
        self.assertEqual(1.0, file.duration_seconds, "Test.wav was not opened correctly!")

    def test_beat_offset(self):
        self.assertEqual(300, wb.beat_offset(200), "The beat offset was calculated incorrectly!")

    def tearDown(self):
        del self.wav_path, self.path, self.bpm
