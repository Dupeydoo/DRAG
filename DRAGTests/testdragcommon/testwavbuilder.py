import unittest
from DRAGProj.dragcommon import wavbuilder as wb
from DRAG import datacontext as dc


class TestWavBuilder(unittest.TestCase):
    def setUp(self):
        context = dc.context
        self.wavpath = context["systempath"] + context["wavpath"]
        self.path = self.wavpath + "test.wav"
        self.bpm = 200

    def testopenwav(self):
        file = wb.openwav(self.path)
        self.assertEqual(1.0, file.duration_seconds, "Test.wav was not opened correctly!")

    def testbeatoffset(self):
        self.assertEqual(300, wb.beatoffset(200), "The beat offset was calculated incorrectly!")

    def tearDown(self):
        del self.wavpath, self.path, self.bpm
