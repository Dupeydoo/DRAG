import unittest
from DRAGProj.generators import genregenerator as gg


class TestGenreGenerator(unittest.TestCase):
    def setUp(self):
        self.structure = [1, 5, 6, 7, 8, 9, 10, 11]
        self.timesig = 8
        self.index = 3
        self.commonvalue = 7

    def testbuildtracklength(self):
        track = gg.buildtrack(self.structure, self.timesig, self.index, self.commonvalue)
        correctlength = True if len(track.content) == 8 else False
        self.assertTrue(correctlength)

    def testbuildtrackcommon(self):
        track = gg.buildtrack(self.structure, self.timesig, self.index, self.commonvalue)
        correctvalue = True if track.content[self.index] == self.commonvalue else False
        self.assertTrue(correctvalue)

    def testgeneratetracks(self):
        population = gg.generaterocktracks([], 5, 8)
        correctlength = True if len(population) == 5 else False
        self.assertTrue(correctlength)

    def tearDown(self):
        del self.structure, self.timesig, self.index, self.commonvalue
