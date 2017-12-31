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