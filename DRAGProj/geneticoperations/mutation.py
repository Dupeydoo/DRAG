import random
import DRAGProj.mappers.drummapper as dm

from DRAGProj.dragcommon.track import Track


def domutation(children, mutaprob):
    mutatedchildren = []
    for child in children:
        if random.random() < mutaprob:
            mutatedchildren.append(mutate(child))

        else:
            mutatedchildren.append(child)

    return mutatedchildren

def mutate(child):
    randindex = random.randrange(0, len(child.content))
    instruments = list(dm.drummapper.keys())
    child.content[randindex] = random.choice(instruments)
    return child

def drumgroupmutate(child):
    instruments = dm.drummapper
    randindex = random.randrange(0, len(child.content))
    groups = creategroups(instruments, child, randindex)
    if dm.isSymbal(groups[2]):
        child.content[randindex] = random.choice(groups[0])
    else:
        child.content[randindex] = random.choice(groups[1])
    return child

def creategroups(instruments, child, randindex):
    hihats = [d[0] for d in instruments.items() if "HHat" in d[1]]
    drums = [d[0] for d in instruments.items() if not "HHat" in d[1]]
    childdrum = child.content[randindex]
    return (hihats, drums, childdrum)
