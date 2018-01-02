import random as rand
from DRAGProj.dragcommon.track import Track

def generaterocktracks(population, tracknumber, timesig):
    structure = [1, 5, 6, 7, 8, 9, 10, 11]
    for track in range(tracknumber):
        track = buildtrack(structure, timesig, 0, 7)
        population.append(track)
    return population

def generatebluestracks(population, tracknumber, timesig):
    structure = [7, 11, 16]
    for track in range(tracknumber):
        track = buildtrack(structure, timesig, 1, 11)
        population.append(track)
    return population

def generatejazztracks(population, tracknumber, timesig):
    structure = [1, 2, 3, 4, 7, 11, 16]
    for track in range(tracknumber):
        track = buildtrack(structure, timesig, 3, 11)
        population.append(track)
    return population

def buildtrack(structure, timesig, index, commonvalue=None):
    track = Track([], 0)
    for beat in range(timesig-1):
        instrument = rand.choice(structure)
        track.addtocontents(instrument)
    track.insertintocontents(index, commonvalue)
    return track


