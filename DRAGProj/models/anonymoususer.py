from django.db import models


class AnonymousUser(models.Model):
    UUID = models.CharField(max_length=32)
