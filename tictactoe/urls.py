"""tictactoe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# Import player views
from player import views

from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from .views import welcome


urlpatterns = [
    path('admin/', admin.site.urls),
    path('player/home', views.home, name='player_home'),
    path('', welcome, name="tictactoe_welcome"),

    # As LogoutView is a Class no a function
    # we need to call `as_view` on it ton convert it to a function
    path('player/login',
        LoginView.as_view(template_name="player/login_form.html"),
        name="player_login"),


    path(r'logout',
        LogoutView.as_view(),
        name="player_logout"),

    path('player/new_invitation', views.new_invitation, name="player_new_invitation"),

    path('player/accept_invitation/<int:id>',
            views.accept_invitation,
            name="player_accept_invitation")
]
