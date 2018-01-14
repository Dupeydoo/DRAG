import unittest
from DRAGProj.dragcommon.track import Track


class TestTrack(unittest.TestCase):
    def setUp(self):
        self.track = Track([1, 2, 3, 4, 5, 6, 7, 8], 5)
        self.tracktwo = Track([1, 2, 3, 4, 5, 6, 7, 8], 6, 3)

    def testinit(self):
        self.assertEqual(1, self.track.trackid, "The id was set incorrectly!")

    def testinitidmethod(self):
        self.assertEqual(3, self.tracktwo.trackid, "The custom id was not set correctly!")

    def testaddtocontents(self):
        self.track.addtocontents(5)
        exists = True if 5 in self.track.content else False
        self.assertEqual(True, exists, "5 was not added to the contents!")

    def testinsertintocontents(self):
        for i in range(10):
            self.track.addtocontents(i+1)
        self.track.insertintocontents(3, 5)
        inserted = True if self.track.content[3] == 5 else False
        self.assertEqual(True, inserted, "The track was not added to the contents at the correct position!")

    def testpairchanged(self):
        Track.pairchanged([self.track, self.tracktwo])
        changed = True if self.track.hasChanged and self.tracktwo.hasChanged else False
        self.assertEqual(True, changed, "The hasChanged values were not set to True")

    def tearDown(self):
        del self.track, self.tracktwo
        Track.idcounter = 0
