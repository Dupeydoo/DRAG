import unittest


class TestStrConcat(unittest.TestCase):
    def setUp(self):
        self.string_one = "Hello "
        self.string_two = "World!"

    def test_str_concat(self):
        def str_concat(string, another_string):
            return str(string) + str(another_string)

        self.assertEqual("Hello World!", str_concat(self.string_one, self.string_two))

    def tearDown(self):
        del self.string_one, self.string_two
