from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import GameForm
from .models import Game


def superuser_required(view_func):
    return user_passes_test(lambda user: user.is_superuser)(view_func)


def game_list(request):
    games = Game.objects.all()
    return render(request, "games/game_list.html", {"games": games})


def game_details(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, "games/game_details.html", {"game": game})


@superuser_required
def game_form(request, game_id=None):
    game = get_object_or_404(Game, id=game_id) if game_id else None
    form = GameForm(request.POST or None, instance=game)

    if request.method == "POST" and form.is_valid():
        game = form.save()
        return redirect("game_details", game_id=game.id)

    return render(request, "games/game_form.html", {"form": form})


def about(request):
    return render(request, "games/about.html")


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("game_list")

    return render(request, "games/login.html", {"form": form})

