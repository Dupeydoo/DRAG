import random
from math import sqrt
from math import pow
import numpy.random as np

def domutation(children, mutaprob):
    for child in children:
        if random.random() < mutaprob:
            children = mutate(child)

def mutate(child):
    mean = sum(child) / len(child)
    sd = sqrt(variance(child, mean))
    pick = np.normal(mean, sd, 1000)

    return mutatemaths(child, pick)

def mutatemaths(child, number):
    if random.random() < 0.5:
        for instrument in child:
            instrument += number

    else:
        for instrument in child:
            instrument -= number

def variance(child, mean):
    for instrument in child:
        instrument = pow((instrument-mean), 2)

    return sum(child) / len(child)


