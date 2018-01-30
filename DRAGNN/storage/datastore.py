import pandas as pd
import numpy as np
import DRAG.datacontext as dc

context = dc.context
store_path = context["system_path"] + "/DRAGNN/storage/"
test_path = context["system_path"] + "/DRAG/static/testdata/"
store = pd.HDFStore(store_path + "data.h5")


def store_data(population, d_store):
    fitness = []
    for track in population:
        content = pd.Series(track.content)
        d_store.append("track", content)
        fitness.append(track.fitness)

    fitness = pd.Series(fitness)
    store.append("fitness", fitness)


def read_data(time_sig, d_store):
    content = list(d_store.select("track"))
    tracks = [content[i:i + time_sig] for i in range(0, len(content), time_sig)]
    fitnesses = list(d_store.select("fitness"))
    return convert_to_np(tracks, fitnesses)


def convert_to_np(tracks, fitnesses):
    track_np = np.array(tracks)
    fitness_np = np.array(fitnesses).reshape(len(fitnesses), 1)
    return track_np, fitness_np


def get_data_store():
    return store


def delete_data_store():
    d_store = get_data_store()
    d_store.remove("track")
    d_store.remove("fitness")


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
