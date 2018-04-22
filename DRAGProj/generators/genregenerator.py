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


def generate_rock_tracks(population, track_number, time_sig):
    """
    This function generates rock style tracks using a structure of instruments.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        track_number (int): The number of tracks to generate.
        time_sig (int): The time signature used in track generation.

    Returns:
        population (:obj:`list` of :obj:`Track`): The population of tracks with genre tracks added.
    """
    structure = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    population = generate_tracks(population, track_number, structure, time_sig)
    return population


def generate_blues_tracks(population, track_number, time_sig):
    """
    DEPRECATED: Only rock is used in production.

    This function generates blues style tracks using a structure of instruments.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        track_number (int): The number of tracks to generate.
        time_sig (int): The time signature used in track generation.

    Returns:
        population (:obj:`list` of :obj:`Track`): The population of tracks with genre tracks added.
    """
    # Common blues rhythm instruments
    structure = [7, 11, 16]
    population = generate_tracks(population, track_number, structure, time_sig)
    return population


def generate_jazz_tracks(population, track_number, time_sig):
    """
    DEPRECATED: Only rock is used in production.

    This function generates jazz style tracks using a structure of instruments.

    Args:
        population (:`obj`:list of :obj:`Track`): The population of tracks.
        track_number (int): The number of tracks to generate.
        time_sig (int): The time signature used in track generation.

    Returns:
        population (:obj:`list` of :obj:`Track`): The population of tracks with genre tracks added.
    """
    # Common jazz rhythm instruments
    structure = [1, 2, 3, 4, 7, 11, 16]
    population = generate_tracks(population, track_number, structure, time_sig)
    return population


def build_track(structure, time_sig):
    """
    Builds a track using the structure and an index to insert a common value at.

    Args:
        structure (:obj:`list` of int): A list of genre structural instruments.
        time_sig (int): The time signature used in track generation.

    Returns:
        track (:obj:Track): The constructed track.
    """
    track = Track([], 0)
    for beat in range(time_sig):
        # Choose from the structure.
        instrument = rand.choice(structure)

        # Add the instrument to the track.
        track.add_to_contents(instrument)
    return track


def generate_tracks(population, track_number, structure, time_sig):
    """
    A helper function to abstract the track building logic out of the generation methods.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        track_number (int): The number of tracks to generate.
        structure (:obj:`list` of int): A list of genre structural instruments.
        time_sig (int): The time signature used in track generation.
        index (int): The index to insert a common value at.
        common_value(:obj:): If specified takes the value of a common instrument used.

    Returns:
        population (:obj:`list` of :obj:`Track`): The population of built tracks.
    """
    for track in range(track_number):
        track = build_track(structure, time_sig)
        population.append(track)
    return population
