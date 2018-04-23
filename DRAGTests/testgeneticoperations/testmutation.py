import unittest

from DRAGProj.dragcommon.track import Track
from DRAGProj.geneticoperations import mutation
from DRAGProj.mappers.drummapper import drum_mapper
from DRAGTests.mock.mockpopulation import MockPopulation

"""
Test module for the mutation module from DRAGProj.

    Author:
        James

    Version:
        1.0.0
"""


class TestMutation(unittest.TestCase):
    """
    Tests the mutation module.

    Attributes:
        children (:obj:`list` of :obj:`Track`): The children to test mutation on.
        child (:obj:`Track`): A single child track.
        muta_prob (float): A testing probability of mutation.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.children = MockPopulation().population
        self.child = Track([1, 2, 3, 4, 5, 6, 7, 8], 5, 1)
        self.muta_prob = 1.0

    def test_do_mutation(self):
        """
        Tests the do_mutation function.
        """
        self.children = mutation.do_mutation(self.children, self.muta_prob)
        changed = True if self.children[0].has_changed else False
        self.assertTrue(changed, "The tracks have not bee marked as mutated!")

    def test_mutate(self):
        """
        Tests the mutate function.
        """
        child = self.child
        self.child = mutation.mutate(Track([1, 2, 3, 4, 5, 6, 7, 8], 1, 2))
        self.assertNotEqual(child.content, self.child.content, "The track was not mutated!")

    def test_drum_group_mutate(self):
        """
        Tests the drum_group_mutate function.
        """
        child = self.child
        self.child = mutation.drum_group_mutate(Track([1, 2, 3, 4, 5, 6, 7, 8], 1, 2))
        self.assertNotEqual(child.content, self.child.content, "The track was not mutated!")

    def test_create_groups(self):
        """
        Tests the create_groups function.
        """
        result = mutation.create_groups(drum_mapper, self.child, 5)
        changed_correctly = True if 1 or 5 or 6 or 7 or 8 or 9 or 10 or 11 == result[0][0] else False
        self.assertTrue(changed_correctly)

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.children, self.child, self.muta_prob
