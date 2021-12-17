from django.urls import path

from .views import home_view


urlpatterns = [
    path('', home_view),
    path('<int:tweet_id>', home_view)
]
