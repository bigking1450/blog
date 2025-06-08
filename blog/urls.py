from django.urls import path

from .views import all_posts, create_post, update_post, post_detail

urlpatterns = [
    path('', all_posts, name='home-page'),
    path('create-post/', create_post, name='create-post'),
    path('update-post/<str:pk>/', update_post, name='update-post'),
    path('post/<str:pk>/', post_detail, name='post-detail'),
]
