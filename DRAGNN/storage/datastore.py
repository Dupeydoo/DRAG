import pandas as pd
import numpy as np
import DRAG.datacontext as dc

context = dc.context
storepath = context["systempath"] + "/DRAGNN/storage/"
store = pd.HDFStore(storepath + "data.h5")


def storeData(population, dstore):
    fitness = []
    for track in population:
        content = pd.Series(track.content)
        dstore.append("track", content)
        fitness.append(track.fitness)

    fitness = pd.Series(fitness)
    store.append("fitness", fitness)


def readData(timesig, dstore):
    content = list(dstore.select("content"))
    tracks = [content[i:i + timesig] for i in range(0, len(content), timesig)]
    fitnesses = list(dstore.select("fitness"))
    return converttonp(tracks, fitnesses)


def converttonp(tracks, fitnesses):
    tracknp = np.array(tracks)
    fitnessnp = np.array(fitnesses).reshape(len(fitnesses), 1)
    return tracknp, fitnessnp


def getdatastore():
    return store

def deletedatastore(path):
    dstore = getdatastore()
    dstore.remove("track")
    dstore.remove("fitness")



if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    lst2 = [8, 7, 6, 5, 4, 3, 2, 1]
    lst3 = [1, 2, 3, 4, 8, 7, 6, 5]

    s = pd.Series(lst)
    t = pd.Series(lst2)
    u = pd.Series(lst3)

    store.append("tracks", s)
    store.append("tracks1", t)
    store.append("tracks2", u)

    print(list(store.select("tracks")))
    print(list(store.select("tracks1")))
    print(list(store.select("tracks2")))

    store.close()
