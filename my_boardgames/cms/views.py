from django.shortcuts import render, redirect
from .models import Game, History, Result
from django.shortcuts import get_object_or_404
from .forms import GameForm, HistoryForm, ResultForm
from django.views.decorators.http import require_POST
from django.db.models import Count, Sum, Q

# Create your views here.
def index(request):
    games = Game.objects.all().order_by('-updated_datetime')
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            upload_image = form.save()
            return redirect('cms:index')
    else:
        form = GameForm
    return render(request, 'cms/index.html', { 'games': games,'form': form })


def detail(request, game_id,):
    game = get_object_or_404(Game, id=game_id)
    histories = History.objects.filter(game=game_id)
    # Query to retrieve results by date
    results = Result.objects.filter(history__game=game_id).order_by('history__date', 'player__name')

    return render(request, 'cms/detail.html', {'game': game, 'histories': histories, 'results': results})

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
            return redirect('cms:detail', game_id)
    else:
        form = GameForm(instance=game)
    return render(request, 'cms/edit_game.html', {'form': form, 'game':game })

def add_history(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    history_id = History.id
    if request.method == "POST":
        history = HistoryForm(request.POST)
        if history.is_valid():
            history.save()
            return redirect('cms:add_result', pk=history_id)
    else:
        history = HistoryForm
    
    return render(request, 'cms/add_history.html', {'form': history, 'game':game })

def add_result(request, history_id):
    history = get_object_or_404(History, id=history_id)
    if request.method == "POST":
        result = ResultForm(request.POST)
        if result.is_valid():
            result.save()
            return redirect('cms:detail.html')
    else:
        result = ResultForm
    return render(request, 'cms/add_result.html', {'form': result, 'history': history,})