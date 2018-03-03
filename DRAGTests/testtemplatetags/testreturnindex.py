import unittest


class TestReturnIndex(unittest.TestCase):
    def setUp(self):
        self.content = [1, 2, 3, 4, 5, 6, 7, 8]
        self.index = 4

    def test_return_index(self):
        def return_index(lst, index):
            return lst[index]

        self.assertEqual(5, return_index(self.content, self.index), "The index returned should have value 5!")

    def tearDown(self):
        del self.content, self.index
