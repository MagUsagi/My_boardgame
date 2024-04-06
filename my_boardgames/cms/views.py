from django.shortcuts import render, redirect
from .models import Game, History, Result
from django.shortcuts import get_object_or_404
from .forms import GameForm, HistoryForm, ResultForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse

# Create your views here.
def index(request):
    games = Game.objects.all().order_by('-updated_datetime')
    # Form to add a new Game
    form = GameForm

    return render(request, 'cms/index.html', { 'games': games,'form': form })

def detail(request, game_id,):
    game = get_object_or_404(Game, id=game_id)
    histories = History.objects.filter(game=game_id)
    # Query to retrieve results by date
    results = Result.objects.filter(history__game=game_id).order_by('-score')
    # # Form to edit the Game
    # form = GameForm(instance=game)
    # history_form = HistoryForm
    # result_form = ResultForm
    # history_form = HistoryForm(request.POST or None)
    # result_form = ResultForm(request.POST or None)

    # if request.method == "POST":
    #     if history_form.is_valid() and result_form.is_valid():
    #         history_instance = history_form.save(commit=False)
    #         history_instance.game = game
    #         history_instance.save()

    #         result_instance = result_form.save(commit=False)
    #         result_instance.history = history_instance
    #         result_instance.save()
    #         return redirect('detail', game_id=game_id)

    return render(request, 'cms/detail.html', {'game': game, 'histories': histories, 'results': results})

### Game ####
def new_game(request):
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            upload_image = form.save()
            return redirect('cms:index')
    else:
        form = GameForm
    return render(request, 'cms/new_game.html', {'form': form })

def edit_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            upload_image = form.save()
            return redirect('cms:detail', game_id)
    else:
        form = GameForm(instance=game)
    return render(request, 'cms/index.html', {'form': form, 'game':game })

@require_POST
def delete_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    game.image.delete()
    game.delete()
    return redirect('cms:index')

### History ####
def add_history(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    history_id = History.id
    if request.method == "POST":
        history = HistoryForm(request.POST)
        if history.is_valid():
            history.save()
            return redirect('cms:detail', pk=history_id)
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

def save_records(request):
    if request.method == 'POST':
        # HistoryFormとResultFormのデータを取得
        history_form = HistoryForm(request.POST)
        result_form = ResultForm(request.POST)

        # 両方のフォームが有効であれば保存
        if history_form.is_valid() and result_form.is_valid():
            history_instance = history_form.save(commit=False)
            result_instance = result_form.save(commit=False)

            # フォームの関連付け
            result_instance.history = history_instance
            
            # 保存
            history_instance.save()
            result_instance.save()

            return JsonResponse({'message': 'Records saved successfully!'})
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)