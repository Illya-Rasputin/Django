
from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('about/', views.about, name='about'),
    path('games/<int:game_id>/', views.game_details, name='game_details'),
    path('games/add/', views.game_form, name='game_add'),
    path('games/<int:game_id>/edit/', views.game_form, name='game_edit'),
    path("login/", views.login_view, name="login")
]
