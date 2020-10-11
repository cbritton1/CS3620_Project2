from django import forms
from .models import StoryOne


class StoryOneForm(forms.ModelForm):
    class Meta:
        model = StoryOne
        fields = ['noun_one', 'noun_two', 'noun_three', 'place', 'adjective', 'noun_four']
