import unittest
import ntpath
from DRAGTests.mock import mockaudiothread
from DRAG import datacontext as dc


class TestAudioThread(unittest.TestCase):
    def setUp(self):
        self.thread = mockaudiothread.MockAudioThread()

    def test_run(self):
        context = dc.context
        path = context["system_path"] + context["wav_path"] + "test.wav"
        self.thread.run()
        self.assertEqual(ntpath.basename(path), "test.wav", "The file was not written!")

    def tearDown(self):
        del self.thread
