from django.forms import ModelForm
from django import forms
from .models import Game, Player, History, Result

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['image', 'title', 'player', 'time', 'memo']
        widgets = {
        'image': forms.FileInput( attrs={'class': 'form-control', 'aria-label': 'image', 'aria-describedby': 'image'}),
        'title': forms.TextInput( attrs={'class': 'form-control', 'aria-label': 'title', 'aria-describedby': 'title'}),
        'player': forms.TextInput( attrs={'class': 'form-control', 'aria-label': 'player', 'aria-describedby': 'player'}),
        'category': forms.Select( attrs={'class': 'form-select', 'aria-label': 'category', 'aria-describedby': 'category'}),
        'time': forms.TextInput( attrs={'class': 'form-control', 'aria-label': 'time', 'aria-describedby': 'time'}),
        'memo': forms.Textarea( attrs={'class': 'form-control', 'aria-label': 'memo', 'aria-describedby': 'memo'})
        }

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields =['name']

class DateInput(forms.DateInput):
    input_type = 'date'

class HistoryForm(ModelForm):
    class Meta:
        model = History
        fields = ['date', 'game', 'duaration']
        widgets = {
            'date': DateInput( attrs={'class': 'form-control', 'aria-label': 'date', 'aria-describedby': 'date'}),
            'game': forms.Select( attrs={'class': 'form-select', 'aria-label': 'game', 'aria-describedby': 'game'}),
            'duaration': forms.NumberInput( attrs={'class': 'form-control', 'aria-label': 'duaration', 'aria-describedby': 'duaration'})
        }

class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = ['history', 'player', 'score', 'winner']
        widgets = {
            'player': forms.Select( attrs={'class': 'form-select', 'aria-label': 'player', 'aria-describedby': 'player'}),
            'score': forms.NumberInput( attrs={'class': 'form-control', 'aria-label': 'score', 'aria-describedby': 'score'}),
            'winner': forms.CheckboxInput( attrs={'class': 'form-check-input', 'aria-label': 'winner', 'id': 'winner'}) 
        }