from pydub import AudioSegment
from pydub import playback
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
    playback.play(output)
    writewav = output.export(outputfile, format="wav")

def beatoffset(bpm):
    return 60000 / bpm