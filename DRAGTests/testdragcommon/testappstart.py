from django.test import TestCase

from DRAGProj.dragcommon.appstart import AppStart

"""
Test module for the AppStart class from DRAGProj.

    Author:
        James
    
    Version:
        1.0.0
"""


class TestAppStart(TestCase):
    """
    Class to test AppStart.

    Attributes:
        start (:obj:`AppStart`): The AppStart object.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.start = AppStart()

    def test_run(self):
        """
        Tests the application start AppStart change.
        """
        self.assertEquals(True, self.start.clear, "The DRAGProj config sets "
                                                  "clear = True!")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.start
