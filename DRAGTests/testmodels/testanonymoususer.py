from django.test import TestCase

from DRAGProj.models.anonymoususer import AnonymousUser

"""
Test module for the AnonymousUser class from DRAGProj.

    Author:
        James

    Version:
        1.0.0
"""


class TestAnonymousUser(TestCase):
    """
    Tests the AnonymousUser class.

    Attributes:
        user (:obj:`AnonymousUser`): An anonymous user to test with.
    """
    def setUp(self):
        """
        Run before each test method. Sets up required resources.
        """
        self.user = AnonymousUser()

    def test_anonymous_user(self):
        """
        Tests the AnonymousUser constructor.
        """
        instance = True if isinstance(self.user, AnonymousUser) else False
        self.assertTrue(instance, "The Anonymous User should be an instance of Anonymous User")

    def tearDown(self):
        """
        Run after each test method. Releases the test resources.
        """
        del self.user
