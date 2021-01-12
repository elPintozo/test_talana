# Django
from django.urls import path

# Apps.players
from apps.players import views

app_name='players'

urlpatterns = [
    path('add/', views.create_player, name='add-player'),
    path('winner/', views.search_to_winner, name='winner-player'),
]