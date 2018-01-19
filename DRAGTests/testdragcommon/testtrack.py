import unittest
from DRAGProj.dragcommon.track import Track


class TestTrack(unittest.TestCase):
    def setUp(self):
        self.track = Track([1, 2, 3, 4, 5, 6, 7, 8], 5)
        self.track_two = Track([1, 2, 3, 4, 5, 6, 7, 8], 6, 3)

    def test_init(self):
        self.assertEqual(1, self.track.track_id, "The id was set incorrectly!")

    def test_init_id_method(self):
        self.assertEqual(3, self.track_two.track_id, "The custom id was not set correctly!")

    def test_add_to_contents(self):
        self.track.add_to_contents(5)
        exists = True if 5 in self.track.content else False
        self.assertEqual(True, exists, "5 was not added to the contents!")

    def test_insert_into_contents(self):
        for i in range(10):
            self.track.add_to_contents(i+1)
        self.track.insert_into_contents(3, 5)
        inserted = True if self.track.content[3] == 5 else False
        self.assertEqual(True, inserted, "The track was not added to the contents at the correct position!")

    def test_pair_changed(self):
        Track.pair_changed([self.track, self.track_two])
        changed = True if self.track.has_changed and self.track_two.has_changed else False
        self.assertEqual(True, changed, "The has_changed values were not set to True")

    def tearDown(self):
        del self.track, self.track_two
        Track.id_counter = 0
