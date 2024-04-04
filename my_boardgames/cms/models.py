from django.db import models
from django.utils import timezone

# Create your models here.
class Game(models.Model):
    image = models.ImageField(upload_to='images', null=True, blank=True)
    title = models.CharField(max_length=150)
    player = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    memo = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Player(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class History(models.Model):
    date = models.DateField(default=timezone.now)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    duaration = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk) + " - " + str(self.date) + " (" + str(self.game) + ")"

class Result(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField()
    winner = models.BooleanField()

    # def __str__(self):
    #     return self.