def generatepopulation(psize, cratio, inputlist, genre):
    copyappend = cratio * psize
    copyappend = int(copyappend)
    population = []

    population = populatecopies(population, copyappend, inputlist)
    population = generategenretracks(population, (psize-copyappend), genre)
    return population


def generategenretracks(population, tracknumber, genre):
    return population


def populatecopies(population, copynumber, inputlist):
    for candidate in range(copynumber):
        population.append(inputlist)
    return population
