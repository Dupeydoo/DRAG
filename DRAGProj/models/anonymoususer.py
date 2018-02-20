from django.db import models

"""
The module that houses the AnonymousUser class.

    Author:
        James

    Version:
        1.0.0
"""


class AnonymousUser(models.Model):
    """
    Class to represent an anonymous visitor to DRAG. An anonymous visitor
    is assigned a unique id so that their track generation information
    is kept private.

    Attributes:
        UUID (:obj:`CharField`): The database field that stored the id.
    """
    UUID = models.CharField(max_length=32)
