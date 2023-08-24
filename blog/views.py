from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm


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
    comments = post.comments.filter(active=True)
    return render(request, "blog/posts/detail.html", {"post":post,
                                                      "form":CommentForm(),
                                                      "comments":comments})
                                                      

def post_share(request, post_id):
    send = False
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            message = f"You can find it on {request.build_absolute_uri(post.get_absolute_url())}"
            if cd['comment'].strip() != "":
                message += f"\n\n{cd['name']}\'s  comments {cd['comment']}"
        
            send_mail(
                f"{cd['name']} recomends you to read {post.title}",
                message,
                cd['email'],
                [cd['to']],
                fail_silently=False
            )
            send = True
    else:
        form = EmailPostForm()
    return render(request, "blog/posts/share.html", {"form":form,
                                                    "post":post,
                                                    "send":send,})
@require_POST
def post_comment(request, post_id):
    """process the comment submitions"""
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, id=post_id)
    form = CommentForm(request.POST)
    comment = None
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        post.save()

    return render(request, "blog/posts/comment.html", {"post":post, "form":form, "comment":comment})

