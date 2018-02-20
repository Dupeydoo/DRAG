import DRAGProj.generators.genregenerator as gg
from DRAGProj.dragcommon.track import Track

"""
This module contains functions to generate a population of Tracks for use in
the genetic algorithm.

    Author:
        James
    
    Version:
        3.4.2
        
    See:
        DRAGProj.generators.genregenerator
"""


def generate_population(p_size, c_ratio, input_list, genre, time_sig):
    """
    This functions generates the population and returns it to the caller.

    Args:
        p_size (int): The size of the population to be generated.
        c_ratio (float): The ratio of input copies to use.
        input_list (:obj:`list` of int): The list of instrument ints to use as input.
        genre (:obj:`str`): The genre of the track to diversify.
        time_sig (int): The time signature used in track generation.

    Returns:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
    """
    copy_append = int(c_ratio * p_size)           # The number of copies to insert into the population.
    population = []

    population = populate_copies(population, copy_append, input_list)  # Create the copies.
    population = generate_genre_tracks(population, (p_size - copy_append), genre,
                                       time_sig)  # Add genre generated remainder.
    return population


def generate_genre_tracks(population, track_number, genre, time_sig):
    """
    Inspects the genre and generates the required genre tracks.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        track_number (int): The number of tracks to generate.
        genre (:obj:`str`): The genre of the track to diversify.
        time_sig (int): The time signature used in track generation.

    Returns:
        population (:obj:`list` of :obj:`Track`): The population of tracks with genre tracks added.
    """
    if genre == "Rock":
        population = gg.generate_rock_tracks(population, track_number, time_sig)

    elif genre == "Blues":
        population = gg.generate_blues_tracks(population, track_number, time_sig)

    elif genre == "Jazz":
        population = gg.generate_jazz_tracks(population, track_number, time_sig)

    return population


def populate_copies(population, copy_number, input_list):
    """
    Creates copies of the input_list to fill the first generation.

    Args:
        population (:obj:`list` of :obj:`Track`): The population of tracks.
        copy_number (int): The number of copies to generate.
        input_list (:obj:`list` of int): The list of instrument ints to use as input.

    Returns:
        population (:obj:`list` of :obj:`Track`): The population of tracks with copies added.

    See:
        DRAGProj.dragcommon.track
    """
    for candidate in range(copy_number):
        track = Track(input_list, 0)  # Create a new track.
        population.append(track)
    return population
