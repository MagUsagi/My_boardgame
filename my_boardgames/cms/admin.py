from django.contrib import admin
from .models import Game, Player, History, Result

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_datetime', 'updated_datetime')
    list_display_links = ('id', 'title')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'game', 'duaration')
    list_display_links = ('id', 'date')

class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'history', 'player', 'score', 'winner')

admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Result, ResultAdmin)