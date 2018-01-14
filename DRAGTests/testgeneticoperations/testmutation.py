import unittest
from DRAGProj.mappers.drummapper import drummapper
from DRAGProj.geneticoperations import mutation
from DRAGProj.dragcommon.track import Track
from DRAGTests.mock.mockpopulation import MockPopulation


class TestMutation(unittest.TestCase):
    def setUp(self):
        self.children = MockPopulation().population
        self.child = Track([1, 2, 3, 4, 5, 6, 7, 8], 5, 1)
        self.mutaprob = 1.0

    def testdomutation(self):
        self.children = mutation.domutation(self.children, self.mutaprob)
        changed = True if self.children[0].hasChanged else False
        self.assertTrue(changed, "The tracks have not bee marked as mutated!")

    def testmutate(self):
        child = self.child
        self.child = mutation.mutate(Track([1, 2, 3, 4, 5, 6, 7, 8], 1, 2))
        self.assertNotEqual(child.content, self.child.content, "The track was not mutated!")

    def testdrumgroupmutate(self):
        child = self.child
        self.child = mutation.drumgroupmutate(Track([1, 2, 3, 4, 5, 6, 7, 8], 1, 2))
        self.assertNotEqual(child.content, self.child.content, "The track was not mutated!")

    def testcreategroups(self):
        result = mutation.creategroups(drummapper, self.child, 5)
        changedcorrectly = True if 1 or 5 or 6 or 7 or 8 or 9 or 10 or 11 == result[0][0] else False
        self.assertTrue(changedcorrectly)

    def tearDown(self):
        del self.children
