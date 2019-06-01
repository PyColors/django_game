"""
This file content a view
He is a function call welcome allow users to see "Hello world"
"""

from django.http import HttpResponse

def welcome(request):
    return HttpResponse("hello world")
