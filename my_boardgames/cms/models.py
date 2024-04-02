from django.db import models

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
    
class History(models.Model):
    date = models.DateField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    duaration = models.CharField(max_length=50)

    def __str__(self):
        return str(self.date) + " (" + str(self.game_id) + ")"

class Result(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    player = models.CharField(max_length=100)
    score = models.IntegerField(default=None, blank=True, null=True)
    winner = models.BooleanField()

    def __str__(self):
        return self.player