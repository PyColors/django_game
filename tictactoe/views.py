"""
This file content a view
Import render function and render welcome HTML
"""

from django.shortcuts import render


def welcome(request):
    return render(request, 'tictactoe/welcome.html')
