from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<slug:post_slug>", views.post_detail, name="post_detail"),

]