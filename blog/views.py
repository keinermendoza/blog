from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    return render(request, "blog/home.html")

def post_list(request):
    posts = Post.publisehd.all()
    return render(request, "blog/posts/list.html", {"posts":posts})

def post_detail(request, post_slug):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post_slug)
    return render(request, "blog/posts/detail.html", {"post":post})
