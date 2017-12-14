from pydub import AudioSegment
import DRAGProj.mappers.drummapper as dm

def openwav(filepath):
    return AudioSegment.from_wav(filepath)

def mapinput(candidate, bpm, outputfile, systempath):
    for instrument in candidate:
        file = dm.drummapper[instrument]
        audio = openwav(systempath + "/DRAG/static/wavfiles/" + file)


