from django import views
from django.contrib import admin
from django.urls import path
from games_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.game_list, name='game_list'),
    path('about/', views.about, name='about'),
    path('games/<int:game_id>/', views.game_details, name='game_details'),
]
