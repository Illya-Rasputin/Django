from django.shortcuts import render
from games_app.models import Game

games = [
    {
        'id': 1,
        'name': 'The Witcher 3',
        'developer': 'CD Projekt Red',
        'description': 'An open-world action RPG set in a dark fantasy world.',
        'release_date': '2015-05-19',
        'rating': 9.5,
        'image_url': 'https://example.com/witcher3.jpg',
    },
    {
        'id': 2,
        'name': 'Minecraft',
        'developer': 'Mojang Studios',
        'description': 'A sandbox game where players can build and explore infinite worlds.',
        'release_date': '2011-11-18',
        'rating': 9.0,
        'image_url': 'https://example.com/minecraft.jpg',
    },
    {
        'id': 3,
        'name': 'Grand Theft Auto V',
        'developer': 'Rockstar Games',
        'description': 'An open-world action-adventure game set in Los Santos.',
        'release_date': '2013-09-17',
        'rating': 9.3,
        'image_url': 'https://example.com/gta5.jpg',
    },
    {
        'id': 4,
        'name': 'Red Dead Redemption 2',
        'developer': 'Rockstar Games',
        'description': 'An open-world western adventure following Arthur Morgan and his gang.',
        'release_date': '2018-10-26',
        'rating': 9.8,
        'image_url': 'https://example.com/rdr2.jpg',
    },
]


def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

def game_details(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/game_details.html', {'game': game})

def about(request):
    return render(request, 'games/about.html')
