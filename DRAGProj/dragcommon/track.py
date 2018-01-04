class Track:
    idcounter = 0

    def __init__(self, content, fitness, idmethod=None):
        self.content = content
        self.fitness = fitness
        self.idmethod = idmethod
        self.hasChanged = False

        if idmethod == None:
            self.__incrementidcounter()
            self.trackid = Track.idcounter

        else:
            self.trackid = self.idmethod

    def addtocontents(self, instrument):
        self.content.append(instrument)

    def insertintocontents(self, index, commonvalue):
        self.content.insert(index, commonvalue)

    def __incrementidcounter(self):
        Track.idcounter += 1

    @staticmethod
    def pairchanged(tracklist):
        for track in tracklist:
            track.hasChanged = True