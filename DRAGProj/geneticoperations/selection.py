import random
from operator import itemgetter

def doselection(population, fitnesses, tournamentsize):
    parents = []
    for selections in range(len(population)):
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
    population = [[2,4,3,6,4,7,8],[7,4,8,5,1,9,4,5],[6,4,7,5,3,5,7,8],[1,2,4,3,6,8,7,9], [3,4,2,5,1,7,6,12], [14,12,13,9,4,3,5,6],
                  [3,6,1,8,15,2,14,5], [4,5,2,7,6,8,3,7], [2,8,7,9,3,6,2,7], [12,13,15,11,10,9,6,7]]
    fitnesses = [4, 10, 3, 7, 5, 7, 8, 1, 9, 0]
    tournmentsize = 2

    parents = doselection(population, fitnesses, tournmentsize)
    print(parents)