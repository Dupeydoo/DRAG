def doreplacement(currentpopulation, children):
    newpopulation = currentpopulation
    for candidate in range(len(newpopulation)):
        newpopulation[candidate] = children[candidate]

    return newpopulation