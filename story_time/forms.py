from django import forms
from .models import StoryOne, StoryTwo, StoryWar, StoryDragons, StoryWalmart, StoryLoveLetter,\
    StorySmellyCat, StoryGreetingsEarthlings, HailToTheChief, HolidayFestivities, PizzaParlor


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


class StoryWalmartForm(forms.ModelForm):
    class Meta:
        model = StoryWalmart
        fields = ['story_name', 'verb1', 'verb2', 'verb3', 'adjective1', 'adjective2', 'adjective3',
                  'adjective4', 'adjective5', 'noun1', 'noun2', 'noun3', 'noun4', 'noun5', 'number',
                  'relative']
        labels = {'story_name': 'Name your story', 'noun1': 'Noun(Plural)', 'verb1': 'Verb ending in "ing"',
                  'noun2': 'Noun(Plural)', 'noun3': 'Noun(Plural)', 'noun4': 'Noun(Plural)', 'noun5': 'Noun(Plural)',
                  'relative': 'Relative(Plural)'}


class StoryLoveLetterForm(forms.ModelForm):
    class Meta:
        model = StoryLoveLetter
        fields = ['story_name', 'person', 'adjective1', 'verb1', 'part_of_the_body', 'number', 'noun1',
                  'adverb', 'verb2', 'pronoun1', 'person2']
        labels = {'story_name': 'Name your story', 'person': 'Person in room', 'person2': 'Other person in room',
                  'pronoun1': 'Pronoun(Plural)'}


class StorySmellyCatForm(forms.ModelForm):
    class Meta:
        model = StorySmellyCat
        fields = ['story_name', 'animal', 'verb1', 'noun1', 'verb2', 'occupation', 'adjective1',
                  'animal2', 'noun2', 'noun3', 'relationship', 'body_part', 'verb3', 'noun4']
        labels = {'story_name': 'Name your story', 'verb1': 'Verb ending in "ing"', 'noun3': 'Noun(Plural)',
                  'body_part': 'Body part(Plural)', 'verb3': 'Verb ending in "ing"'}


class StoryGreetingsEarthlingsForm(forms.ModelForm):
    class Meta:
        model = StoryGreetingsEarthlings
        fields = ['story_name', 'occupation', 'animal', 'place', 'verb1', 'noun2']
        labels = {'story_name': 'Name your story', 'animal': 'Animal(Plural)'}


class HailToTheChiefForm(forms.ModelForm):
    class Meta:
        model = HailToTheChief
        fields = ['story_name', 'place', 'time', 'adjective1', 'noun1', 'noun2', 'noun3',
                  'noun4', 'verb1', 'verb2', 'occupation']
        labels = {'story_name': 'Name your story', 'time': 'Amount of time', 'noun3': 'Noun(Plural)',
                  'noun4': 'Noun(Plural)'}


class HolidayFestivitiesForm(forms.ModelForm):
    class Meta:
        model = HolidayFestivities
        fields = ['story_name', 'month', 'number', 'holiday', 'noun1', 'noun2', 'noun3', 'noun4', 'noun5',
                  'verb1', 'verb2', 'occupation']
        labels = {'story_name': 'Name your story', 'noun1': 'Noun(Plural)', 'verb1': 'Verb ending in "ing"',
                  'noun2': 'Noun(Plural)'}


class PizzaParlorForm(forms.ModelForm):
    class Meta:
        model = PizzaParlor
        fields = ['story_name', 'male_name', 'adjective1', 'noun1', 'adjective2', 'food', 'noun2', 'verb1', 'liquid',
                  'noun3']
        labels = {'story_name': 'Name your story', 'food': 'Food(Plural)', 'noun2': 'Noun(Plural)',
                  'verb1': 'Verb ending in "ing"'}
