import threading

from pydub import AudioSegment

from DRAG import datacontext as dc

"""
Mock module for the AudioThread class.

    Author:
        James
        
    Version:
        1.0.0
"""


class MockAudioThread(threading.Thread):
    """
    Class to  mock the AudioThread class for simplicity
    in unit tests.

    Attributes:
        output (:obj:`AudioSegment`): The object to write
        to a file.

        output_file (:obj:`str`): The file path to write to.
    """
    def __init__(self):
        """
        MockAudioThread constructor, initialises the output
        and the path.
        """
        threading.Thread.__init__(self)
        context = dc.context
        path = context["system_path"] + context["wav_path"] + "test.wav"

        # Make a silent wav to write for testing.
        self.output = AudioSegment.silent(duration=1000)
        self.output_file = path

    def run(self):
        """
        Runs the thread to write the wav file.
        """
        write_wav = self.output.export(self.output_file, format="wav")
