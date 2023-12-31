from django.db import models
from django.db.models.query import QuerySet
from django.db.models import Count
from django.utils import timezone
from django.utils.text import Truncator
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
        

class User(AbstractUser):
    def __str__(self):
        return self.username


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")

    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"])
        ]

    def __str__(self):
        return Truncator(self.title).words(5,truncate="")
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.slug, self.publish.day, self.publish.month, self.publish.year])

    def serialize(self):
        return {
            "title": self.title,
            "author": self.author.username,
            "body": Truncator(self.body).words(20, truncate=" ..."),
            "publish": self.publish,
            "url": self.get_absolute_url(),
        }
    
class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    objects = models.Manager()
    oactive = ActiveCommentManager()

    class Meta:
        ordering = ["created"]
        indexes = [
            models.Index(fields=["created"])
        ]


    def __str__(self):
        return f"Comment of {self.user.username} on {self.post.title}"

    def serialize(self):
        return {
            "name":self.name,
            "body":self.body,
            "created": self.created,
            "count": Comment.objects.filter(id__in=[self.post.id]).count()
        }