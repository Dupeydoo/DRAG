import DRAGProj.generators.populationgenerator as pg
import DRAGProj.dragcommon.wavbuilder as wb
import DRAGProj.dragcommon.dragmaths as dm
import DRAG.datacontext as dc
import os

from DRAGProj.geneticoperations import selection
from DRAGProj.geneticoperations import crossover
from DRAGProj.geneticoperations import mutation
from DRAGProj.geneticoperations import generationalreplacement

context = dc.context
systempath = context["systempath"]
populationsize = context["populationsize"]
copyratio = context["copyratio"]
tournamentsize = context["tournamentsize"]
timesignature = context["timesignature"]
crossprob = context["crossprob"]
mutaprob = context["mutaprob"]

def initiliasepopulation(inputlist, genre, bpm):
    if dm.iseven(populationsize) and populationsize != 0:
        population = pg.generatepopulation(populationsize, copyratio, inputlist, genre, timesignature)
        return population
    #raise error
    return

def processinput(population, bpm):
    wavpath = systempath + "/DRAG/static/wavfiles/"
    for candidate in range(len(population)):
        solution = population[candidate]
        outputfile = wavpath + "candidate" + str(candidate) + ".wav"
        wb.mapinput(solution, bpm, outputfile, systempath)


def performgenetics(population):
    parents = selection.doselection(population, tournamentsize)
    children = crossover.docrossover(parents, crossprob)
    children = mutation.domutation(children, mutaprob)
    newpopulation = generationalreplacement.doreplacement(population, children)
    return newpopulation

def clearwavfiles():
    wavpath = systempath + "/DRAG/static/wavfiles/"
    wb.clearwavcandidates(wavpath, "candidate")
