import random
from operator import itemgetter

from DRAGProj.dragcommon.track import Track

def doselection(population, tournamentsize):
    parents = []
    for selections in range(len(population)):
        parent = tournamentselect(population, tournamentsize)
        parent.hasChanged = False
        parents.append(parent)
    return parents

def tournamentselect(population, tournamentsize):
    randomselections = []
    for candidates in range(tournamentsize):
        randindex = random.randrange(0, len(population))
        randomselections.append((randindex, population[randindex].fitness))
    return tournament(population, randomselections)

def tournament(population, selections):
    index = max(selections, key=itemgetter(1))[0]
    return population[index]