import random
import DRAGProj.mappers.drummapper as dm
from math import sqrt
from math import pow
import numpy.random as np


def domutation(children, mutaprob):
    mutatedchildren = []
    for child in children:
        if random.random() < mutaprob:
            mutatedchildren.append(mutate(child))

        else:
            mutatedchildren.append(child)

    return mutatedchildren

def mutate(child):
    randindex = random.randrange(0, len(child))
    instruments = list(dm.drummapper.keys())
    child[randindex] = random.choice(instruments)
    return child


"""
def mutate(child):
    mean = average(child)
    sd = sqrt(variance(child, mean))
    pick = np.normal(mean, sd, 1000)
    print((mean, sd, pick))

    return mutatemaths(child, pick)


def mutatemaths(child, number):
    randindex = random.randrange(0, len(child))
    if random.random() < 0.5:
        child[randindex] += number

    else:
        child[randindex] -= number

    return child


def variance(child, mean):
    variancelist = []
    for instrument in child:
        variancelist.append(pow((instrument - mean), 2))

    return average(variancelist)


def average(child):
    return sum(child) / len(child)
"""

if __name__ == "__main__":
    children = [[2,5,3,9,12,15,6,4], [4,5,2,8,2,12,6,8]]
    mutaprob = 0.9

    children = domutation(children, mutaprob)
    print(children)