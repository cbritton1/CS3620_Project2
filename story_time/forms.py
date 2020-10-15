from django import forms
from .models import StoryOne, StoryTwo, StoryWar, StoryDragons


class StoryOneForm(forms.ModelForm):
    class Meta:
        model = StoryOne
        fields = ['story_name', 'noun_one', 'noun_two', 'noun_three', 'place', 'adjective', 'noun_four']
        labels = {"story_name": "Name your story"}


class StoryTwoForm(forms.ModelForm):
    class Meta:
        model = StoryTwo
        fields = ['story_name', 'silly_word1', 'last_name', 'illness', 'noun_plural', 'adjective1', 'adjective2',
                  'silly_word2', 'place', 'number', 'adjective3']
        labels = {'story_name': 'Name your story', 'noun_plural': 'noun(plural)'}


class StoryWarForm(forms.ModelForm):
    class Meta:
        model = StoryWar
        fields = ['story_name', 'noun1', 'noun2', 'noun3', 'occupation', 'verb', 'verb2', 'noun4', 'verb3', 'noun5',
                  'noun6', 'emotion']
        labels = {'story_name': 'Name your story', 'verb2': 'Verb ending in "ed"', 'verb3': 'Verb ending in "ing"', 'noun5': 'Noun (plural)'}


class StoryDragonsForm(forms.ModelForm):
    class Meta:
        model = StoryDragons
        fields = ['story_name', 'color', 'superlative', 'adjective1', 'body_part', 'body_part2', 'noun1', 'animal',
                  'adjective2', 'adjective3', 'adjective4']
        labels = {'story_name': 'Name your story', 'superlative': 'Superlative (ending in "est")',
                  'body_part': 'Body Part(plural)', 'animal': 'Animal(plural)'}
