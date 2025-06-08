from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Post, Tag
from .forms import PostForm
# Create your views here.


def all_posts(request):
    p = Paginator(Post.objects.all(), 9)  # 9 posts per page
    page = request.GET.get('page')
    posts = p.get_page(page)

    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    tags = Tag.objects.all()

    context = {
        'post': post,
        'tags': tags
    }
    return render(request, 'blog/post_detail.html', context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # form.save_m2m()
            return redirect('home-page')
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'blog/create-post.html', context)


def update_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # form.save_m2m()
            return redirect('home-page')
    else:
        form = PostForm(instance=post)

    context = {'form': form}
    return render(request, 'blog/create-post.html', context)
