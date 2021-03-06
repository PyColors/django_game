from django.conf.urls import url
from django.contrib.auth.views import LogoutView, LoginView

from .views import game_detail

urlpatterns = [
    url('detail/(?P<id>\d+)/$',
        game_detail,
        name="gameplay_detail"),

    url('make_move/(?P<id>\d+)/$',
        make_move,
        name="gameplay_make_move")
]