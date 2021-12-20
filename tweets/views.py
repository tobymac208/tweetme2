import random as rn

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import TweetForm
from .models import Tweet

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    # grab the desired location from the form
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)
        # save data to our database
        obj.save()
        # AJAX response! #
        if request.is_ajax():
            # 201 == created items
            return JsonResponse(obj.serialize(), status=201)
        # verify there's a url AND that it's a safe url
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            # redirect the user to wherever the form said to go
            return redirect(next_url)
        # clear the form
        form = TweetForm()
    return render(request, 'components/form.html', context={'form': form})


def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Reason: Allows ubiquitous consumption by JavaScript, Swift, Java, or iOS/Android, etc.
    Return JSON data.
    """
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]

    data = {
        'isUser': False,
        'response': tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Reason: Allows ubiquitous consumption by JavaScript, Swift, Java, or iOS/Android, etc.
    Return JSON data.
    """

    data = {
        'id': tweet_id,
    }

    status = 200

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'not found'
        status = 404
    return JsonResponse(data, status=status)
