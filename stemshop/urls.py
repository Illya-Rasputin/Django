from django import views
from django.contrib import admin
from django.urls import path, include
from games_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('games_app.urls'))
]
