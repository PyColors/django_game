"""
This file content a view
Import render function and render welcome HTML
"""

from django.shortcuts import render, redirect


def welcome(request):

    # Check if the user authenticated
    if request.user.is_authenticated:

        # so redirect to the correct page (player_home)
        #`player_home` he's not a URL, but name of the URL to go on
        return redirect('player_home')
    else:
        # Default home page
        return render(request, 'tictactoe/welcome.html')
