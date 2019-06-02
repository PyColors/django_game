from django.conf.urls import url

from .views import home


# List of all views
urlPatterns = [
    url(r'home$', home)
]