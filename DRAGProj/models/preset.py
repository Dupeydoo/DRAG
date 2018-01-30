from django.db import models


class Preset(models.Model):
    beat_one = models.PositiveSmallIntegerField()
    beat_two = models.PositiveSmallIntegerField()
    beat_three = models.PositiveSmallIntegerField()
    beat_four = models.PositiveSmallIntegerField()
    beat_five = models.PositiveSmallIntegerField()
    beat_six = models.PositiveSmallIntegerField()
    beat_seven = models.PositiveSmallIntegerField()
    beat_eight = models.PositiveSmallIntegerField()
