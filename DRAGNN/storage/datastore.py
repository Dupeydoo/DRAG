import pandas as pd
import numpy as np
import DRAG.datacontext as dc
import os

"""
Datastore module used as single point of access to HDF5 files in
the filesystem. Fitness data is written here over the course of
manual generations, and read from for automated generations.
"""

context = dc.context
store_path = context["system_path"] + "/DRAGNN/storage/"
test_path = context["system_path"] + "/DRAG/static/testdata/"

# The path to be used when the module is executed.
current_path = store_path


def store_data(population, user_id):
    """
    Stores population data in a HDF5 file uniquely identified
    by user id. Data is stored as pandas Series objects for
    tracks and fitness values.

    Args:
        population (:obj:`list` of :obj:`Track`): The GA population.
        user_id (:obj:`str`): The user identifier string.
    """
    fitness = []

    # Make a new HDF5 file and append Series data to it.
    store = pd.HDFStore(current_path + str(user_id) + "data.h5")
    for track in population:
        content = pd.Series(track.content)
        store.append("track", content)
        fitness.append(track.fitness)

    fitness = pd.Series(fitness)
    store.append("fitness", fitness)
    store.close()


def read_data(time_sig, user_id):
    """
    Reads track and fitness data from a HDF5 format into a
    numpy array format. Reads only the current user's file.

    Args:
        time_sig (int): The number of beats per bar. 4:4.
        user_id (:obj:`str`): The user identifier string.

    Returns:
        :obj:`tuple` of :obj:`ndarray`: A tuple of ndarrays
        containing fitness and track data.
    """
    store = pd.HDFStore(current_path + str(user_id) + "data.h5")
    content = list(store.select("track"))

    # Split the track data into a list of lists at time_sig length.
    tracks = [content[i:i + time_sig] for i in range(0, len(content), time_sig)]
    fitnesses = list(store.select("fitness"))
    store.close()
    return convert_to_np(tracks, fitnesses)


def convert_to_np(tracks, fitnesses):
    """
    Converts track and fitness data into a matrix like numpy array format
    for scikit-learn processing.

    Args:
        tracks (:obj:`list` of :obj:`list`): List of track lists.
        fitnesses (:obj:`list` of int): List of fitness values.

    Returns:
        (track_np, fitness_np) (:obj:`tuple` of :obj:`ndarray`): A tuple
        of ndarrays containing fitness and track data.
    """
    track_np = np.array(tracks).astype(float)
    fitness_np = np.array(fitnesses).reshape(len(fitnesses), 1).astype(float)
    return track_np, fitness_np


def get_data_store(user_id):
    """
    Accessor for a user's data store used outside the datastore
    module.

    Args:
        user_id (:obj:`str`): The user identifier used to select the
        data store.

    Returns:
        :obj:`HDFStore`: The HDF5 store associated with the user id.
    """
    return pd.HDFStore(current_path + str(user_id) + "data.h5")


def delete_data_store(user_id):
    """
    Deletes the data store specified by the user identifier.

    Args:
        user_id (:obj:`str`): The identifier of the data store
        to remove.
    """
    store = get_data_store(user_id)
    store.close()
    os.remove(current_path + str(user_id) + "data.h5")
