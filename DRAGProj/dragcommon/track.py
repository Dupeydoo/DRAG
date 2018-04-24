"""
A module housing the Track class.

    Author:
        James

    Version:
        2.1.0
"""


class Track:
    """
    A class to represent a music track within DRAG.

    Attributes:
        content (:obj:`list` of int): The tracks encoding.
        fitness (int): A value between 0 and 10 representing the users
        satisfaction.

        id_method (:obj:): Either a None when not specified, or an int
        when specified.

        has_changed (bool): False when unchanged from last generation.
        track_id (int): track identifier.
    """
    # Static attribute to keep track of used ids.
    id_counter = 0

    def __init__(self, content, fitness, id_method=None):
        """
        Constructor for Track class.

        Args:
            content (:obj:`list` of int): The tracks encoding.
            fitness (int): A value between 0 and 10 representing the users
            satisfaction.

            id_method (:obj:): Either a None when not specified, or a readable
            string when specified.
        """
        self.content = content
        self.fitness = fitness
        self.id_method = id_method
        self.has_changed = False

        if id_method is None:
            # Normal id method, increment the id_counter.
            self.__increment_id_counter()
            self.track_id = Track.id_counter

        else:
            # Otherwise use the provided id.
            self.track_id = self.id_method

    def add_to_contents(self, instrument):
        """
        Adds an instrument to the track content.

        Args:
            instrument (int): An int representing an instrument from the
            drummapper.
        """
        self.content.append(instrument)

    def insert_into_contents(self, index, common_value):
        """
        Inserts an instrument at the given index of a tracks content.

        Args:
            index (int): An index to insert the instrument at.
            common_value (int): An int representing an instrument from the
            drummapper often a common value.
        """
        self.content.insert(index, common_value)

    @staticmethod
    def __increment_id_counter():
        """
        Increments the static id_counter attribute when called.
        """
        Track.id_counter += 1

    @staticmethod
    def pair_changed(track_list):
        """
        Static method to take a pair of tracks and change has_changed.

        Args:
            track_list (:obj:`list` of :obj:`Track`): A list (usually a pair)
            of tracks.
        """
        for track in track_list:
            track.has_changed = True
