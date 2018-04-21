from django.test import TestCase
from DRAGProj.models.anonymoususer import AnonymousUser


class TestAnonymousUser(TestCase):
    def setUp(self):
        self.user = AnonymousUser()

    def test_anonymous_user(self):
        instance = True if isinstance(self.user, AnonymousUser) else False
        self.assertTrue(instance, "The Anonymous User should be an instance of Anonymous User")

    def tearDown(self):
        del self.user
