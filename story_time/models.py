from django.db import models


# Create your models here.
class StoryOne(models.Model):
    noun_one = models.CharField(max_length=20)
    noun_two = models.CharField(max_length=20)
    noun_three = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    adjective = models.CharField(max_length=20)
    noun_four = models.CharField(max_length=20)
