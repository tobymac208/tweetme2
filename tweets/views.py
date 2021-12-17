from django.http import HttpResponse
from django.shortcuts import render

from .models import Tweet


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello, world!</h1>")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    reponse = ''

    try:
        obj = Tweet.objects.get(id=tweet_id)
        response = f'Details for {tweet_id} are {obj.content}'
    except:
        response = 'not found'
    return HttpResponse(f'<h1>{response}</h1>')
