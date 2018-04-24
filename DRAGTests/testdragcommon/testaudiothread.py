import ntpath
import unittest

from DRAG import datacontext as dc
from DRAGTests.mock import mockaudiothread

"""
Test module for the AudioThread class from DRAGProj.

    Author:
        James

    Version:
        1.0.0
"""


class TestAudioThread(unittest.TestCase):
    """
    Tests the AudioThread class.

    Attributes:
        thread (:obj:`MockAudioThread`): The MockAudioThread object.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.thread = mockaudiothread.MockAudioThread()

    def test_run(self):
        """
        Tests that AudioThread run method.
        """
        context = dc.context
        path = context["system_path"] + context["wav_path"] + "test.wav"
        self.thread.run()
        self.assertEqual(ntpath.basename(path), "test.wav",
                         "The file was not written!")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.thread
