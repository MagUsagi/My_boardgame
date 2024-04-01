from django.forms import ModelForm
from .models import Game

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['image', 'title','player', 'time', 'memo']