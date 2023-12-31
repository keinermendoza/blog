from django.contrib import admin
from .models import Post, Comment, User

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):



    list_display = ["title", "author", "created", "publish", "status"]
    list_filter = ["created", "author", "publish", "status"]
    search_fields = ["title", "body"]
    date_hierarchy = "publish"
    raw_id_fields = ["author"]
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["status", "publish"]
    # fieldsets = [
    #     (None,
    #      {
    #          "fields": ["title", "body", "author", "status", "slug", "tags"]
    #      }),
    # ]
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created", "active"]
    list_filter = ["created", "updated", "active"]
    search_fields = ["body", "user"]

admin.site.register(User)
