from django.forms import ModelForm
from django import forms
from .models import Game, History, Result

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['image', 'title', 'player', 'time', 'memo']

class DateInput(forms.DateInput):
    input_type = 'date'

class HistoryForm(ModelForm):
    class Meta:
        model = History
        fields = ['date', 'game', 'duaration']
        widgets = {
            'date': DateInput(),
        }

class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = ['player', 'score', 'winner']