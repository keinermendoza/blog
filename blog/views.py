import markdown
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Post, Comment, User
from .forms import EmailPostForm, CommentForm, RegisterForm, LoginForm
from taggit.models import Tag
from django.db.models import Count
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline

def home(request):
    return render(request, "blog/home.html")

def post_list(request):
    posts = Post.published.all()
    
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

def post_list_by_tag(request, tag_slug=None):
    tag = None
    post_list = Post.published.all()
    
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    
    paginate_by = 3
    page = request.GET.get("page", 1)
    paginator = Paginator(post_list, paginate_by)
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages())

    return render(request, "blog/posts/list.html", {"posts":posts,
                                                    "tag":tag})

def post_detail(request, post_slug, day, month, year):
    post = get_object_or_404(Post,
                            status=Post.Status.PUBLISHED,
                            slug=post_slug,
                            publish__day=day,
                            publish__month=month,
                            publish__year=year)
    
    comments = post.comments.filter(active=True)

    tags_id = post.tags.values_list("id", flat=True) # id of all the tags of this object
    similar_posts = Post.published.filter(tags__in=tags_id).exclude(id=post.id)
    similar_posts = similar_posts.annotate(common_tags=Count("tags"))\
        .order_by("-common_tags", "-publish")
    
    return render(request, "blog/posts/detail.html", {"post":post,
                                                      "comment_form":CommentForm(),
                                                      "share_form":EmailPostForm(),
                                                      "comments":comments,
                                                      "similar_posts":similar_posts})
                                                      
@require_POST
def post_comment(request, post_id):
    """process the comment submitions"""
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, id=post_id)
    form = CommentForm(request.POST)
    comment = None
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post

        if request.user.is_authenticated:
            comment.user = request.user
            message = "Comentario publicado con exito"
        else:
            comment.user = User.objects.get(id=2) # anonimos user
            comment.active = False
            message = "Comentario publicado como usuario anonimo, será publicado luego de pasar por revision"


        comment.save()
        messages.add_message(request, constants.SUCCESS, message)

        return JsonResponse({"message":"Comentario publicado con Exito"}, status=200)
    else:
        errors = form.errors.get_json_data()
        return JsonResponse(errors, status=400, safe=False)

@login_required
@require_POST
def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    form = EmailPostForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        
        message = f"acabas de recibir una recomendacion de lectura del Blog de Keiner Mendoza. Puedes encontrar la publicacion en {request.build_absolute_uri(post.get_absolute_url())}"
        message_end = f"\n\nEn caso que no conozca a {request.user} o no tenga entre sus contactos a {request.user.email} puede ignorar este correo"
        
        if cd['comentario'].strip() != "":
            message += f"\n\n{request.user}\' comenta sobre esta publicacion que: {cd['comentario']}"
    
        send_mail(
            f"{request.user} te recomienda leer {post.title}",
            message + message_end,
            request.user.email,
            [cd['destinatario']],
            fail_silently=False
        )
        return JsonResponse({"message":"Recomendación enviada con exito."})
    else:
        errors = form.errors.get_json_data()
        return JsonResponse(errors, status=400, safe=False)

@require_GET
def search_post(request):
    query = request.GET.get("query")    
    if query:
        vector = SearchVector("title", "body", config='spanish')
        query = SearchQuery(query, config='spanish')
        headline = SearchHeadline("body",
                                  query,
                                  start_sel="<span class='bg-warning text-dark'>",
                                  stop_sel="</span>",
                                  max_words=50,
                                  min_words=30)

        posts = Post.published.annotate(search=vector, rank=SearchRank(vector, query))\
        .annotate(headline=headline).filter(search=query).order_by("-rank")

        return JsonResponse([{"title":post.title,
                              "body":markdown.markdown(post.headline),
                              "author":post.author.username,
                              "publish":post.publish,
                              "url":post.get_absolute_url()} for post in posts], safe=False, status=200)
    else:
        return JsonResponse({"error":"query field required"}, status=400)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd["nombre"], password=cd["contraseña"])
            user.email = cd["email"]
            user.save()
        
            login(request, user)
            messages.add_message(request, constants.SUCCESS, f"Welcome {user.username}")
            return redirect(reverse("post_list"))
    else:
        form = RegisterForm()
    return render(request, "blog/login_or_register.html", {"form":form})

def login_view(request):
    if request.user.is_authenticated: # avoid the users already loged
        return redirect(reverse("post_list"))
    
    if request.method == "POST":

        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if user := authenticate(username=cd["nombre"], password=cd["contraseña"]):
                print(user)
                login(request, user)
                messages.add_message(request, constants.SUCCESS, f"Bienvenido {user.username}")
                return redirect(reverse("post_list"))
        else:
            messages.add_message(request, constants.ERROR, "Lo siento, email o contraseña invalida.")
    else:
        form = LoginForm()
    return render(request, "blog/login_or_register.html", {"form": form,
                                            "show_register_link":True})
@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse("post_list"))