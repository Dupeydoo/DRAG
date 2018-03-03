from django.db import models

"""
The module that houses the Preset class.

    Author:
        James

    Version:
        1.0.0
"""


class Preset(models.Model):
    """
    Class to represent a preset. Each beat of the preset is stored
    in a database column. Each beat is stored as a small number in
    the database for optimisation.

    Attributes:
        beat_one (:obj:`PositiveSmallIntegerField`): The first beat.
        beat_two (:obj:`PositiveSmallIntegerField`): The second beat.
        beat_three (:obj:`PositiveSmallIntegerField`): The third beat.
        beat_four (:obj:`PositiveSmallIntegerField`): The fourth beat.
        beat_five (:obj:`PositiveSmallIntegerField`): The fifth beat.
        beat_six (:obj:`PositiveSmallIntegerField`): The sixth beat.
        beat_seven (:obj:`PositiveSmallIntegerField`): The seventh beat.
        beat_eight (:obj:`PositiveSmallIntegerField`): The eighth beat.
    """
    beat_one = models.PositiveSmallIntegerField()
    beat_two = models.PositiveSmallIntegerField()
    beat_three = models.PositiveSmallIntegerField()
    beat_four = models.PositiveSmallIntegerField()
    beat_five = models.PositiveSmallIntegerField()
    beat_six = models.PositiveSmallIntegerField()
    beat_seven = models.PositiveSmallIntegerField()
    beat_eight = models.PositiveSmallIntegerField()
