from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import InvitationForm
from .models import Invitation
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
    # Check request method
    if request.method == "POST":
        # Create an invitation object and setting user that's logged in `from_user=request.user`
        invitation = Invitation(from_user=request.user)

        # Validation: New instance with data argument,
        # Now the form object is an instance of InvitationForm()
        form = InvitationForm(instance=invitation, data=request.POST)


        # If all fields have been filled correctly or even with blank input
        if form.is_valid():
            # create a model instance and save into the database
            form.save()
            return redirect('player_home')

    else:

        # New instance of InvitationForm Class (HTML fo invitation)
        form = InvitationForm()
    return render(request, "player/new_invitation_form.html", {'form': form})
