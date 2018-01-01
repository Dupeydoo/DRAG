import random

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
    randindex = random.randrange(0, len(parents[0]))
    children = recombine(parents, randindex)
    return children

def multipointcrossover(parents):
    firstindex = random.randrange(0, len(parents[0]))
    secondindex = random.randrange(firstindex, len(parents[0]))
    children = multirecombine(parents, firstindex, secondindex)
    return children

def recombine(parents, index):
    firstparent = parents[0]
    secondparent = parents[1]
    firstchild = firstparent[:index] + secondparent[index:]
    secondchild = secondparent[:index] + firstparent[index:]
    return [firstchild, secondchild]

def multirecombine(parents, idxone, idxtwo):
    firstparent = parents[0]
    secondparent = parents[1]
    firstchild = firstparent[:idxone] + secondparent[idxone:idxtwo] + firstparent[idxtwo:]
    secondchild = secondparent[:idxone] + firstparent[idxone:idxtwo] + secondparent[idxtwo:]
    return [firstchild, secondchild]



if __name__ == "__main__":
    parents = [[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]]

    parents = multipointcrossover(parents)
    print(parents)