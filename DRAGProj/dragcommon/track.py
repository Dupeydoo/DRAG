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
        content (:obj:list of int): The tracks encoding.
        fitness (int): A value between 0 and 10 representing the users satisfaction.
        idmethod (:obj:): Either a None when not specified, or an int when specified.
        haschanged (bool): False when unchanged from last generation.
        trackid (int): track identifier.
    """
    idcounter = 0    # Static attribute to keep track of used ids.

    def __init__(self, content, fitness, idmethod=None):
        """
        Constructor for Track class.

        Args:
            content (:obj:list of int): The tracks encoding.
            fitness (int): A value between 0 and 10 representing the users satisfaction.
            idmethod (:obj:): Either a None when not specified, or a readable string when specified.
        """
        self.content = content
        self.fitness = fitness
        self.idmethod = idmethod
        self.hasChanged = False

        if idmethod == None:
            self.__incrementidcounter()     # Normal id method, increment the idcounter.
            self.trackid = Track.idcounter

        else:
            self.trackid = self.idmethod    # else use the provided id.

    def addtocontents(self, instrument):
        """
        Adds an instrument to the track content.

        Args:
            instrument (int): An int representing an instrument from the drummapper.
        """
        self.content.append(instrument)

    def insertintocontents(self, index, commonvalue):
        """
        Inserts an instrument at the given index of a tracks content.

        Args:
            index (int): An index to insert the instrument at.
            commonvalue (int): An int representing an instrument from the drummapper often a common value.
        """
        self.content.insert(index, commonvalue)

    def __incrementidcounter(self):
        """
        Increments the static idcounter attribute when called.
        """
        Track.idcounter += 1

    @staticmethod
    def pairchanged(tracklist):
        """
        Static method to take a pair of tracks and change haschanged.

        Args:
            tracklist (:obj:list of :obj:Track): A list (usually a pair) of tracks.
        """
        for track in tracklist:
            track.hasChanged = True