from django.http import JsonResponse
from .models import Post

def published_posts(request):
    """"this function is a kind of copy of post data of post_list
    fot use JavaScript pagination"""
    
    published = Post.publisehd.all()
    return JsonResponse({"published": [p.serialize() for p in published]})