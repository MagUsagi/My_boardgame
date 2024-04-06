from django.urls import path
from . import views

app_name = 'cms'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>', views.detail, name='detail'),
    path('new_game', views.new_game, name='new_game'),
    path('delete_game/<int:game_id>', views.delete_game, name='delete_game'),
    path('edit_game/<int:game_id>', views.edit_game, name='edit_game'),
    path('add_history/<int:game_id>', views.add_history, name='add_history'),
    path('add_result/<int:history_id>', views.add_result, name='eadd_result'),
    path('save_records/', views.save_records, name='save_records'),
]

