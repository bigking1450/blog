from django.urls import path

from .views import all_posts, create_post

urlpatterns = [
    path('', all_posts, name='home-page'),
    path('create-post/', create_post, name='create-post'),
]
