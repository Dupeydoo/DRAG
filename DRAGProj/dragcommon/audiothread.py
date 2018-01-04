import threading
from pydub import AudioSegment

"""
A module which houses the AudioThread class.

    Author:
        James
    
    Version:
        1.0.0
"""

class AudioThread(threading.Thread):
    """
    A class that extends python's threading.Thread to
    construct an object which writes a wav file on run.

    Attributes:
        output (:obj:`AudioSegment`): A pydub AudioSegment object containing wav file data.
        outputfile (:obj:`str`): A string representing the output wav filename.
    """
    def __init__(self, output, outputfile):
        """
        AudioThread constructor.

        Args:
            output (:obj:`AudioSegment`): A pydub AudioSegment object containing wav file data.
            outputfile (:obj:`str`): A string representing the output wav filename.
        """
        threading.Thread.__init__(self)  # Call the Thread superconstructor.
        self.output = output
        self.outputfile = outputfile

    def run(self):
        """
        Runs the Thread.
        """
        writewav = self.output.export(self.outputfile, format="wav")  # Write the wav file to the static wavfiles dir.

