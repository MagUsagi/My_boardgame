from django.shortcuts import render, redirect
from .models import Game
from django.shortcuts import get_object_or_404
from .forms import GameForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    games = Game.objects.all().order_by('-updated_datetime')
    return render(request, 'cms/index.html', { 'games': games })

def detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'cms/detail.html', {'game': game})

def new_game(request):
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            upload_image = form.save()
            return redirect('cms:index')
    else:
        form = GameForm
    return render(request, 'cms/new_game.html', {'form': form })

@require_POST
def delete_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    game.image.delete()
    game.delete()
    return redirect('cms:index')

def edit_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            upload_image = form.save()
            return redirect('cms:index')
    else:
        form = GameForm(instance=game)
    return render(request, 'cms/edit_game.html', {'form': form, 'game':game })