import random

def docrossover(parents, crossprob):
    children = []
    for parentone, parenttwo in zip(*[iter(parents)] * 2):
        pair = [parentone, parenttwo]
        if random.random() < crossprob:
            children += singlepointcrossover(pair)
    return children

def singlepointcrossover(parents):
    crossoverpoints = []
    randindex = random.randrange(0, len(parents[0]))
    children = recombine(parents, randindex)
    return children

def recombine(parents, index):
    firstparent = parents[0]
    secondparent = parents[1]
    firstchild = firstparent[:index] + secondparent[index:]
    secondchild = secondparent[:index] + firstparent[index:]
    return [firstchild, secondchild]


if __name__ == "__main__":
    parents = [[2, 4, 3, 6, 4, 7, 8], [7, 4, 8, 5, 1, 9, 4, 5], [6, 4, 7, 5, 3, 5, 7, 8], [1, 2, 4, 3, 6, 8, 7, 9], [3, 4, 2, 5, 1, 7, 6, 12],
               [14, 12, 13, 9, 4, 3, 5, 6], [3, 6, 1, 8, 15, 2, 14, 5], [4, 5, 2, 7, 6, 8, 3, 7], [2, 8, 7, 9, 3, 6, 2, 7], [12, 13, 15, 11, 10, 9, 6, 7]]

    crossprob = 0.9
    children = docrossover(parents, crossprob)
    print(children)