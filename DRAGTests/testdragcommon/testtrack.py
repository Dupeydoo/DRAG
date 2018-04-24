import unittest

from DRAGProj.dragcommon.track import Track

"""
Test module for the Track class from DRAGProj.

    Author:
        James

    Version:
        1.3.0
"""


class TestTrack(unittest.TestCase):
    """
    Class to test the Track class.

    Attributes:
        track (:obj:`Track`): An example track.
        track_two (:obj:`Track`): A second example track.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.track = Track([1, 2, 3, 4, 5, 6, 7, 8], 5)
        self.track_two = Track([1, 2, 3, 4, 5, 6, 7, 8], 6, 3)

    def test_init(self):
        """
        Tests the id capabilities of the constructor.
        """
        self.assertEqual(1, self.track.track_id, "The id was set incorrectly!")

    def test_init_id_method(self):
        """
        Tests the custom id method of the constructor.
        """
        self.assertEqual(3, self.track_two.track_id,
                         "The custom id was not set correctly!")

    def test_add_to_contents(self):
        """
        Tests the add_to_contents method.
        """
        self.track.add_to_contents(5)
        exists = True if 5 in self.track.content else False
        self.assertEqual(True, exists, "5 was not added to the contents!")

    def test_insert_into_contents(self):
        """
        Tests the insert_into_contents method.
        """
        # Add some tracks to the object.
        for i in range(10):
            self.track.add_to_contents(i + 1)

        # Insert a different value.
        self.track.insert_into_contents(3, 5)
        inserted = True if self.track.content[3] == 5 else False
        self.assertEqual(True, inserted,
            "The track was not added to the contents at the correct position!")

    def test_pair_changed(self):
        """
        Tests the static pair_changed method.
        """
        Track.pair_changed([self.track, self.track_two])
        changed = True if self.track.has_changed and \
                          self.track_two.has_changed else False
        self.assertEqual(True, changed,
                         "The has_changed values were not set to True")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.track, self.track_two
        Track.id_counter = 0
