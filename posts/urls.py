# posts/urls.py

from django.urls import path
from .views import get_posts, post_detail

urlpatterns = [
    path('<pk>/', post_detail, name='post_detail'),
    path('', get_posts, name='get_posts'),
]
