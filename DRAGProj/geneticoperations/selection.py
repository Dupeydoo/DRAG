import random
from operator import itemgetter

def doselection(population, fitnesses, tournamentsize):
    parents = []
    for selections in range(len(population)):
        parent = tournamentselect(population, fitnesses, tournamentsize)
        parents.append(parent)
    return parents

def tournamentselect(population, fitnesses, tournamentsize):
    randomselections = []
    for candidates in range(tournamentsize):
        randindex = random.randrange(0, len(fitnesses))
        randomselections.append((randindex, fitnesses[randindex]))
    return tournament(population, randomselections)

def tournament(population, selections):
    index = max(selections, key=itemgetter(1))[0]
    return population[index]