import DRAGProj.generators.populationgenerator as pg
import DRAGProj.dragcommon.wavbuilder as wb
import DRAGProj.dragcommon.dragmaths as dm
import DRAG.datacontext as dc

from DRAGProj.geneticoperations import selection
from DRAGProj.geneticoperations import crossover
from DRAGProj.geneticoperations import mutation
from DRAGProj.geneticoperations import generationalreplacement

context = dc.context
systempath = context["systempath"]
wavpath = context["wavpath"]
populationsize = context["populationsize"]
copyratio = context["copyratio"]
tournamentsize = context["tournamentsize"]
timesignature = context["timesignature"]
crossprob = context["crossprob"]
mutaprob = context["mutaprob"]


def initiliasepopulation(inputlist, genre):
    if dm.iseven(populationsize) and populationsize <= 0:
        return pg.generatepopulation(populationsize, copyratio, inputlist, genre, timesignature)
    else:
        popsize = 10
        return pg.generatepopulation(popsize, copyratio, inputlist, genre, timesignature)


def processinput(population, bpm):
    path = systempath + wavpath
    for candidate in range(len(population)):
        solution = population[candidate]
        outputfile = path + "candidate" + str(candidate) + ".wav"
        wb.mapinput(solution, bpm, outputfile, path)


def performgenetics(population):
    parents = selection.doselection(population, tournamentsize)
    children = crossover.docrossover(parents, crossprob)
    children = mutation.domutation(children, mutaprob)
    newpopulation = generationalreplacement.doreplacement(population, children)
    return newpopulation


def clearwavfiles():
    path = systempath + wavpath
    wb.clearwavcandidates(path, "candidate")
