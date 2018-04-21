from django.test import TestCase
from DRAGProj.dragcommon.appstart import AppStart


class TestAppSTart(TestCase):
    def setUp(self):
        self.start = AppStart()

    def test_run(self):
        self.assertEquals(True, self.start.clear, "The DRAGProj config sets clear = True!")

    def tearDown(self):
        del self.start
