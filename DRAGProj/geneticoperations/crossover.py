import random

from DRAGProj.dragcommon.track import Track


def docrossover(parents, crossprob):
    children = []
    singlepointprob = 0.5
    for parentone, parenttwo in zip(*[iter(parents)] * 2):
        pair = [parentone, parenttwo]
        if random.random() < crossprob:
            if random.random() < singlepointprob:
                children += singlepointcrossover(pair)

            else:
                children += multipointcrossover(pair)
        else:
            children += pair
    return children


def singlepointcrossover(parents):
    randindex = random.randrange(0, len(parents[0].content))
    children = recombine(parents, randindex)
    return children


def multipointcrossover(parents):
    firstindex = random.randrange(0, len(parents[0].content))
    secondindex = random.randrange(firstindex, len(parents[0].content))
    children = multirecombine(parents, firstindex, secondindex)
    return children


def recombine(parents, index):
    firstparent = parents[0].content
    secondparent = parents[1].content
    firstchild = Track((firstparent[:index] + secondparent[index:]), parents[0].fitness, parents[0].trackid)
    secondchild = Track((secondparent[:index] + firstparent[index:]), parents[1].fitness, parents[1].trackid)
    return [firstchild, secondchild]


def multirecombine(parents, idxone, idxtwo):
    firstparent = parents[0].content
    secondparent = parents[1].content
    firstchild = Track((firstparent[:idxone] + secondparent[idxone:idxtwo] + firstparent[idxtwo:]), parents[0].fitness,
                       parents[0].trackid)
    secondchild = Track((secondparent[:idxone] + firstparent[idxone:idxtwo] + secondparent[idxtwo:]),
                        parents[1].fitness,
                        parents[1].trackid)
    return [firstchild, secondchild]
