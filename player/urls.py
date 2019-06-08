from django.conf.urls import url

from django.contrib.auth.views import LoginView, LogoutView
from .views import home, accept_invitation


# List of all views
urlPatterns = [
    url(r'home$', home, name="player_home")
]