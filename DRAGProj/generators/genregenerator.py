import random as rand

def generaterocktracks(population, tracknumber, timesig):
    structure = [1, 5, 6, 7, 8, 9, 10, 11]
    for track in range(tracknumber):
        track = buildtrack(structure, timesig, 7)
        population.append(track)
    return population

def generatebluestracks(population, tracknumber, timesig):
    return population

def generatejazztracks(population, tracknumber, timesig):
    return population

def generateclassicaltracks(population, tracknumber, timesig):
    return population

def buildtrack(structure, timesig, commonvalue=None):
    track = []
    track.append(commonvalue)
    for beat in range(timesig-1):
        instrument = rand.choice(structure)
        track.append(instrument)
    return track


