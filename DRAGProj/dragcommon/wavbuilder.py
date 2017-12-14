from pydub import AudioSegment
import DRAGProj.mappers.drummapper as dm

def openwav(filepath):
    return AudioSegment.from_wav(filepath)

def mapinput(candidate, bpm, outputfile):
    for instrument in candidate:
        file = dm.drummapper[instrument]
        audio = openwav("/DRAG/static/wavfiles/" + file)

