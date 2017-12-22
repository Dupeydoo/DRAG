import random
from operator import itemgetter

def doselection(population, fitnesses, tournamentsize):
    parents = []
    for selections in range(len(population) // tournamentsize):
        parents.append(tournamentselect(population, fitnesses, tournamentsize))
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

if __name__ == "__main__":
    population = [[2,4,3,6,4,7,8],[7,4,8,5,1,9,4,5],[6,4,7,5,3,5,7,8],[1,2,4,3,6,8,7,9]]
    fitnesses = [4, 10, 3, 7]
    tournmentsize = 2

    parents = doselection(population, fitnesses, tournmentsize)
    print(parents)