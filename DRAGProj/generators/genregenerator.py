import random as rand
from DRAGProj.dragcommon.track import Track

"""
This module generates tracks based on input genre.

    Author:
        James
        
    Version:
        3.0.0
        
    See:
        DRAGProj.dragcommon.track
"""


def generaterocktracks(population, tracknumber, timesig):
    """
    This function generates rock style tracks using a structure of instruments.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        tracknumber (int): The number of tracks to generate.
        timesig (int): The time signature used in track generation.

    Returns:
        population (:obj:`list` of :obj:`Track`): The population of tracks with genre tracks added.
    """
    structure = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # Common rock rhythm instruments
    population = generatetracks(population, tracknumber, structure, timesig, 0, 2)
    return population


def generatebluestracks(population, tracknumber, timesig):
    """
    This function generates blues style tracks using a structure of instruments.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        tracknumber (int): The number of tracks to generate.
        timesig (int): The time signature used in track generation.

    Returns:
        population (:obj:`list` of :obj:`Track`): The population of tracks with genre tracks added.
    """
    structure = [7, 11, 16]  # Common blues rhythm instruments
    population = generatetracks(population, tracknumber, structure, timesig, 1, 3)
    return population


def generatejazztracks(population, tracknumber, timesig):
    """
    This function generates jazz style tracks using a structure of instruments.

    Args:
        population (:`obj`:list of :obj:`Track`): The population of tracks.
        tracknumber (int): The number of tracks to generate.
        timesig (int): The time signature used in track generation.

    Returns:
        population (:obj:`list` of :obj:`Track`): The population of tracks with genre tracks added.
    """
    structure = [1, 2, 3, 4, 7, 11, 16]  # Common jazz rhythm instruments
    population = generatetracks(population, tracknumber, structure, timesig, 3, 3)
    return population


def buildtrack(structure, timesig, index, commonvalue):
    """
    Builds a track using the structure and an index to insert a common value at.

    Args:
        structure (:obj:`list` of int): A list of genre structural instruments.
        timesig (int): The time signature used in track generation.
        index (int): The index to insert a common value at.
        commonvalue(:obj:): Takes the value of a common instrument used.

    Returns:
        track (:obj:Track): The constructed track.
    """
    track = Track([], 0)
    for beat in range(timesig - 1):
        instrument = rand.choice(structure)  # Choose from the structure.
        track.addtocontents(instrument)  # Add the instrument to the track.
    track.insertintocontents(index, commonvalue)  # Insert the common value into the track.
    return track


def generatetracks(population, tracknumber, structure, timesig, index, commonvalue=None):
    """
    A helper function to abstract the track building logic out of the generation methods.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        tracknumber (int): The number of tracks to generate.
        structure (:obj:`list` of int): A list of genre structural instruments.
        timesig (int): The time signature used in track generation.
        index (int): The index to insert a common value at.
        commonvalue(:obj:): If specified takes the value of a common instrument used.

    Returns:
        population (:obj:`list` of :obj:`Track`): The population of built tracks.
    """
    for track in range(tracknumber):
        track = buildtrack(structure, timesig, index, commonvalue)
        population.append(track)
    return population
