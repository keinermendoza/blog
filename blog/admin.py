from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created", "publish", "status"]
    list_filter = ["created", "author", "publish", "status"]
    search_fields = ["title", "body"]
    date_hierarchy = "publish"
    raw_id_fields = ["author"]
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["status", "publish"]
