from django.db import models


# Create your models here.
class StoryOne(models.Model):
    story_name = models.CharField(max_length=200)
    noun_one = models.CharField(max_length=20)
    noun_two = models.CharField(max_length=20)
    noun_three = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    adjective = models.CharField(max_length=20)
    noun_four = models.CharField(max_length=20)


class StoryTwo(models.Model):
    story_name = models.CharField(max_length=200)
    silly_word1 = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    illness = models.CharField(max_length=30)
    noun_plural = models.CharField(max_length=30)
    adjective1 = models.CharField(max_length=30)
    adjective2 = models.CharField(max_length=30)
    silly_word2 = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    number = models.IntegerField()
    adjective3 = models.CharField(max_length=30)


class StoryWar(models.Model):
    story_name = models.CharField(max_length=200)
    noun1 = models.CharField(max_length=200)
    noun2 = models.CharField(max_length=200)
    noun3 = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    verb = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    verb2 = models.CharField(max_length=200)
    noun4 = models.CharField(max_length=200)
    verb3 = models.CharField(max_length=200)
    noun5 = models.CharField(max_length=200)
    noun6 = models.CharField(max_length=200)
    emotion = models.CharField(max_length=200)


class StoryDragons(models.Model):
    story_name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    superlative = models.CharField(max_length=200)
    adjective1 = models.CharField(max_length=200)
    body_part = models.CharField(max_length=200)
    body_part2 = models.CharField(max_length=200)
    noun1 = models.CharField(max_length=200)
    animal = models.CharField(max_length=200)
    adjective2 = models.CharField(max_length=200)
    adjective3 = models.CharField(max_length=200)
    adjective4 = models.CharField(max_length=200)

