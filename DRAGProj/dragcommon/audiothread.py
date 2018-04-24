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
    A class that extends Python's threading.Thread to
    construct an object which writes a wav file.

    Attributes:
        output (:obj:`AudioSegment`): A pydub AudioSegment object
        containing wav file data.

        output_file (:obj:`str`): A string representing the output
        wav filename.
    """

    def __init__(self, output, output_file):
        """
        AudioThread constructor.

        Args:
            output (:obj:`AudioSegment`): A pydub AudioSegment object
            containing wav file data.

            output_file (:obj:`str`): A string representing the output
            wav filename.
        """
        # Call the Thread super-constructor.
        threading.Thread.__init__(self)
        self.output = output
        self.output_file = output_file

    def run(self):
        """
        Runs the Thread, thus performing the write.
        """
        # Writes the wav file to the static wavfiles dir.
        write_wav = self.output.export(self.output_file,
                                       format="wav")
