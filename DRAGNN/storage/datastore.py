import pandas as pd
import numpy as np
import DRAG.datacontext as dc
import os

context = dc.context
store_path = context["system_path"] + "/DRAGNN/storage/"
test_path = context["system_path"] + "/DRAG/static/testdata/"
current_path = store_path


def store_data(population, user_id):
    fitness = []
    store = pd.HDFStore(current_path + str(user_id) + "data.h5")
    for track in population:
        content = pd.Series(track.content)
        store.append("track", content)
        fitness.append(track.fitness)

    fitness = pd.Series(fitness)
    store.append("fitness", fitness)
    store.close()


def read_data(time_sig, user_id):
    store = pd.HDFStore(current_path + str(user_id) + "data.h5")
    content = list(store.select("track"))
    tracks = [content[i:i + time_sig] for i in range(0, len(content), time_sig)]
    fitnesses = list(store.select("fitness"))
    store.close()
    return convert_to_np(tracks, fitnesses)


def convert_to_np(tracks, fitnesses):
    track_np = np.array(tracks).astype(float)
    fitness_np = np.array(fitnesses).reshape(len(fitnesses), 1).astype(float)
    return track_np, fitness_np


def get_data_store(user_id):
    return pd.HDFStore(current_path + str(user_id) + "data.h5")


def delete_data_store(user_id):
    store = get_data_store(user_id)
    store.close()
    os.remove(current_path + str(user_id) + "data.h5")


# Integration Test
if __name__ == "__main__":
    from DRAGTests.mock.mockpopulation import MockPopulation
    mock = MockPopulation().population
    u_id = "test-user"

    store_data(mock, u_id)
    data = read_data(8, u_id)

    delete_data_store(u_id)
