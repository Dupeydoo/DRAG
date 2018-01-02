import DRAGProj.generators.genregenerator as gg
from DRAGProj.dragcommon.track import Track

def generatepopulation(psize, cratio, inputlist, genre, timesig):
    copyappend = int(cratio * psize)
    population = []

    population = populatecopies(population, copyappend, inputlist)
    population = generategenretracks(population, (psize-copyappend), genre, timesig)
    return population


def generategenretracks(population, tracknumber, genre, timesig):
    if genre == "Rock":
        population = gg.generaterocktracks(population, tracknumber, timesig)

    elif genre == "Blues":
        population = gg.generatebluestracks(population, tracknumber, timesig)

    elif genre == "Jazz":
        population = gg.generatejazztracks(population, tracknumber, timesig)

    return population


def populatecopies(population, copynumber, inputlist):
    for candidate in range(copynumber):
        track = Track(inputlist, 0)
        population.append(track)
    return population
