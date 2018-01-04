import os
from pydub import AudioSegment
from DRAGProj.dragcommon.audiothread import AudioThread
from DRAGProj.dragcommon.track import Track
import DRAGProj.mappers.drummapper as dm

def openwav(filepath):
    return AudioSegment.from_wav(filepath)

def mapinput(candidate, bpm, outputfile, path):
    output = AudioSegment.silent(duration=100)
    gap = AudioSegment.silent(duration=beatoffset(bpm))
    for instrument in candidate.content:
        file = dm.drummapper[instrument]
        audio = openwav(path + file)
        output = output.append(gap)
        output = output.append(audio)
    beginaudiothread(output, outputfile, gap)

def beginaudiothread(output, outputfile, gap):
    output = output.append(gap)
    thread = AudioThread(output, outputfile)
    thread.start()

def beatoffset(bpm):
    return 60000 / bpm

def clearwavcandidates(wavdirectory, string):
    for file in os.listdir(wavdirectory):
        if string in file:
            os.remove(os.path.join(wavdirectory, file))