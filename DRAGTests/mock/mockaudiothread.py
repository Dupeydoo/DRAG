import threading
from pydub import AudioSegment
from DRAG import datacontext as dc


class MockAudioThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        context = dc.context
        path = context["systempath"] + context["wavpath"] + "test.wav"
        self.output = AudioSegment.silent(duration=1000)
        self.outputfile = path

    def run(self):
        writewav = self.output.export(self.outputfile, format="wav")
