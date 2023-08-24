from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post
from .forms import EmailPostForm

def home(request):
    return render(request, "blog/home.html")

def post_list(request):
    posts = Post.publisehd.all()
    
    paginate_by = 2
    page = request.GET.get("page", 1)
    paginator = Paginator(posts, paginate_by)
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)

    return render(request, "blog/posts/list.html", {"posts":posts})

def post_detail(request, post_slug, day, month, year):
    post = get_object_or_404(Post,
                            status=Post.Status.PUBLISHED,
                            slug=post_slug,
                            publish__day=day,
                            publish__month=month,
                            publish__year=year)
    
    return render(request, "blog/posts/detail.html", {"post":post})
                                                      

def post_share(request, post_id):
    send = False
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            send = True
    else:
        form = EmailPostForm()
    return render(request, "blog/posts/share.html", {"form":form,
                                                    "post":post,
                                                    "send":send,})
