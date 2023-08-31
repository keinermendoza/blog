from django.urls import path
from . import views, api_views
from .feed import LatestPostFeed

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("posts/tag/<slug:tag_slug>", views.post_list_by_tag, name="post_list_by_tag"),
    path("post/<slug:post_slug>/<int:day>/<int:month>/<int:year>", views.post_detail, name="post_detail"),
    path('post/<int:post_id>/share', views.post_share, name="post_share"),
    path('post/<int:post_id>/comment', views.post_comment, name="post_comment"),
    path('post/search', views.search_post, name="search_post"),
    path("feed/", LatestPostFeed(), name="posts_feed"),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
]