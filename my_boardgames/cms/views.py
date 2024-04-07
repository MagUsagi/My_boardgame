from django.shortcuts import render, redirect
from .models import Game, History, Result
from django.shortcuts import get_object_or_404
from .forms import GameForm, HistoryForm, ResultForm, RecordFormset
from django.views.decorators.http import require_POST
from django.http import JsonResponse

# Create your views here.
def index(request):
    games = Game.objects.all().order_by('-updated_datetime')
    # Form to add a new Game
    game_form = GameForm

    return render(request, 'cms/index.html', { 'games': games,'game_form': game_form })

def detail(request, game_id,):
    game = get_object_or_404(Game, id=game_id)
    histories = History.objects.filter(game=game_id)
    # Query to retrieve results by date
    results = Result.objects.filter(history__game=game_id).order_by('-score')
    initial_data = {'game': game} 
    record_form = HistoryForm(initial=initial_data)
    record_formset = RecordFormset()
    game_form = GameForm(instance=game)

    context = {
        'game': game,
        'histories': histories,
        'results': results,
        'record_form': record_form,
        'record_formset': record_formset,
        'game_form': game_form,
    }
    return render(request, 'cms/detail.html', context)


### Game ####
def new_game(request):
    if request.method == "POST":
        game_form = GameForm(request.POST, request.FILES)
        if game_form.is_valid():
            upload_image = game_form.save()
            return redirect('cms:index')
    else:
        game_form = GameForm
    return render(request, 'cms/new_game.html', {'game_form': game_form })

def edit_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == "POST":
        game_form = GameForm(request.POST, request.FILES, instance=game)
        if game_form.is_valid():
            upload_image = game_form.save()
            return redirect('cms:detail', game_id)
    else:
        game_form = GameForm(instance=game)
    return render(request, 'cms/index.html', {'game_form': game_form, 'game':game })

@require_POST
def delete_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    game.image.delete()
    game.delete()
    return redirect('cms:index')

### History ####
def add_record(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    form = HistoryForm(request.POST or None, instance=game)
    context = {'form': form}
    form.game = game.id
    if request.method == 'POST' and form.is_valid():
        history = form.save(commit=False)
        formset = RecordFormset(request.POST, instance=history)
        if formset.is_valid():
            history.save()
            formset.save()
            return redirect('cms:detail', game_id)
        else:
            context['formset'] = formset
    else:
        context['formset'] = RecordFormset()
    another_context = {'game': game}
    marged_context = {**another_context, **context}

    return render(request, 'cms/add_record.html', marged_context)