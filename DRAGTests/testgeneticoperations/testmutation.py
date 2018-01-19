import unittest
from DRAGProj.mappers.drummapper import drummapper
from DRAGProj.geneticoperations import mutation
from DRAGProj.dragcommon.track import Track
from DRAGTests.mock.mockpopulation import MockPopulation


class TestMutation(unittest.TestCase):
    def setUp(self):
        self.children = MockPopulation().population
        self.child = Track([1, 2, 3, 4, 5, 6, 7, 8], 5, 1)
        self.muta_prob = 1.0

    def test_do_mutation(self):
        self.children = mutation.do_mutation(self.children, self.muta_prob)
        changed = True if self.children[0].has_changed else False
        self.assertTrue(changed, "The tracks have not bee marked as mutated!")

    def test_mutate(self):
        child = self.child
        self.child = mutation.mutate(Track([1, 2, 3, 4, 5, 6, 7, 8], 1, 2))
        self.assertNotEqual(child.content, self.child.content, "The track was not mutated!")

    def test_drum_group_mutate(self):
        child = self.child
        self.child = mutation.drum_group_mutate(Track([1, 2, 3, 4, 5, 6, 7, 8], 1, 2))
        self.assertNotEqual(child.content, self.child.content, "The track was not mutated!")

    def test_create_groups(self):
        result = mutation.create_groups(drummapper, self.child, 5)
        changed_correctly = True if 1 or 5 or 6 or 7 or 8 or 9 or 10 or 11 == result[0][0] else False
        self.assertTrue(changed_correctly)

    def tearDown(self):
        del self.children
