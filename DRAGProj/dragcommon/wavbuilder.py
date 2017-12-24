import os
import re
from pydub import AudioSegment
from DRAGProj.dragcommon.audiothread import AudioThread
import DRAGProj.mappers.drummapper as dm

def openwav(filepath):
    return AudioSegment.from_wav(filepath)

def mapinput(candidate, bpm, outputfile, systempath):
    output = AudioSegment.silent(duration=100)
    gap = AudioSegment.silent(duration=beatoffset(bpm))
    for instrument in candidate:
        file = dm.drummapper[instrument]
        audio = openwav(systempath + "/DRAG/static/wavfiles/" + file)
        output = output.append(gap)
        output = output.append(audio)
    output = output.append(gap)
    thread = AudioThread(output, outputfile)
    thread.start()

def beatoffset(bpm):
    return 60000 / bpm

def clearwavcandidates(wavdirectory, regpattern):
    for file in os.listdir(wavdirectory):
        if re.search(regpattern, file):
            os.remove(os.path.join(dir, file))

# regpattern for candidates "/^candidate[0-9]*.wav$/"