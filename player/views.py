from django.shortcuts import render

from gameplay.models import Game


def home(request):
    # `Game.objects`: customer manager Class,
    # Allow calling `game_for_user` on it and pass currently logged-in user

    my_games = Game.objects.game_for_user(request.user)
    # Selecting only game that are not finished yet
    active_games = my_games.active()

    return render(request, "player/home.html",
                    {'games': active_games})

