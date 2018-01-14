import unittest
import ntpath
from DRAGTests.mock import mockaudiothread
from DRAG import datacontext as dc


class TestAudioThread(unittest.TestCase):
    def setUp(self):
        self.thread = mockaudiothread.MockAudioThread()

    def testrun(self):
        context = dc.context
        path = context["systempath"] + context["wavpath"] + "test.wav"
        self.thread.run()
        self.assertEqual(ntpath.basename(path), "test.wav", "The file was not written!")

    def tearDown(self):
        del self.thread
