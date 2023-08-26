from django import template
from blog.models import Post
from django.db.models import Count
import markdown
from django.utils.html import format_html

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag("custom_tags/black_alert_posts.html")
def get_latest_posts(max=3):
    posts = Post.published.order_by("-publish")[:max]
    return {"posts":posts}

@register.inclusion_tag("custom_tags/black_alert_posts.html")
def get_posts_most_commented(max=3):
    posts = Post.published.annotate(comment_count=Count("comments")).order_by("-comment_count", "-publish")[:max]
    return {"posts":posts}

@register.filter(name="from_markdown")
def convert_markdown(text):
    return format_html(markdown.markdown(text))

@register.filter()
def pluralize_es(n):
    if n == 1:
        return "es"
    else:
        return ""