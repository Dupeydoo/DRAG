import threading
from pydub import AudioSegment
from DRAG import datacontext as dc


class MockAudioThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        context = dc.context
        path = context["systempath"] + context["wavpath"] + "test.wav"
        self.output = AudioSegment.silent(duration=1000)
        self.output_file = path

    def run(self):
        write_wav = self.output.export(self.output_file, format="wav")
