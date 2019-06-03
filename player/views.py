from django.shortcuts import render

from gameplay.models import Game


def home(request):
    games_first_player = Game.objects.filter(
        first_player=request.user,
        status='F'
    )
    games_second_player = Game.objects.filter(
        first_player=request.user,
        status='S'
    )
    # Combine in one variable
    # converting each QuerySet into a list adding those togetherr

    all_my_games = list(games_first_player) + \
                   list(games_second_player)

    # Pass new list of all players' games to the template
    return render(request, "player/home.html",
        {'games': all_my_games })


