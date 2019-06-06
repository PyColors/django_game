from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import InvitationForm
from gameplay.models import Game


# Decorator `@login_required` users has to be log-in
@login_required
def home(request):
    # `Game.objects`: customer manager Class,
    # Allow calling `game_for_user` on it and pass currently logged-in user

    my_games = Game.objects.game_for_user(request.user)
    # Selecting only game that are not finished yet
    active_games = my_games.active()

    return render(request, "player/home.html",
                    {'games': active_games})


@login_required
def new_invitation(request):
    # New instance of InvitationForm Class (HTML fo invitation)
    form = InvitationForm()
    return render(request, "player/new_invitation_form.html", {'form': form})