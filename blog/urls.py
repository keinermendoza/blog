from django.urls import path
from . import views, api_views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<slug:post_slug>/<int:day>/<int:month>/<int:year>", views.post_detail, name="post_detail"),
    path('post/<int:post_id>/share', views.post_share, name="post_share"),
    # api_views
    path("posts/published_posts", api_views.published_posts, name="published_posts"),

]