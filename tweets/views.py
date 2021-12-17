from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Tweet


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello, world!</h1>")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    response = ''

    try:
        obj = Tweet.objects.get(id=tweet_id)
        response = f'Details for {tweet_id} are {obj.content}'
    except:
        raise Http404
    return HttpResponse(f'<h1>{response}</h1>')
