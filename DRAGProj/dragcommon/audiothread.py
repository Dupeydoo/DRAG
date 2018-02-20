import threading

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
        output_file (:obj:`str`): A string representing the output wav filename.
    """

    def __init__(self, output, output_file):
        """
        AudioThread constructor.

        Args:
            output (:obj:`AudioSegment`): A pydub AudioSegment object containing wav file data.
            output_file (:obj:`str`): A string representing the output wav filename.
        """
        threading.Thread.__init__(self)  # Call the Thread super-constructor.
        self.output = output
        self.output_file = output_file

    def run(self):
        """
        Runs the Thread.
        """
        write_wav = self.output.export(self.output_file,
                                       format="wav")  # Write the wav file to the static wavfiles dir.
