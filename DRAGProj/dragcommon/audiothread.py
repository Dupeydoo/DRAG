import threading
from pydub import AudioSegment

class AudioThread(threading.Thread):
    def __init__(self, output, outputfile):
        threading.Thread.__init__(self)
        self.output = output
        self.outputfile = outputfile
        self.format = format

    def run(self):
        writewav = self.output.export(self.outputfile, format="wav")

