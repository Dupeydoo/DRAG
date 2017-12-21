import random

def docrossover(parents, crossprob):
    if(random.random() < crossprob):
        children = singlepointcrossover(parents)
    return children


def singlepointcrossover(parents):
    crossoverpoints = []
    randindex = random.randrange(0, len(parents[0]))
    children = recombine(parents, randindex)
    return children

def recombine(parents, index):
    firstparent = parents[0]
    secondparent = parents[1]
    firstchild = [firstparent[:index] + secondparent[index:]]
    secondchild = [secondparent[:index] + firstparent[index:]]
    return [firstchild, secondchild]


