from django.forms import ModelForm
from .models import Game, History, Result

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['image', 'title', 'player', 'time', 'memo']

class HistoryForm(ModelForm):
    class Meta:
        model = History
        fields = ['date', 'duaration']

class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = ['player', 'score', 'winner']