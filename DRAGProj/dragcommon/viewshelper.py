from django.http import HttpResponseRedirect

def gatherfitnessinput(dict):
    candidatefitnesses = []
    for fitness in dict:
        candidatefitnesses.append(fitness[1])
    return candidatefitnesses

def generationcheck(currentgeneration, maxgeneration):
    if currentgeneration == maxgeneration:
        return HttpResponseRedirect('/NeuralNetwork')