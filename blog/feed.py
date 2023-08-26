import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy

from blog.models import Post

class LatestPostFeed(Feed):
    title = "Keiner's Blog"
    link = reverse_lazy("post_list")
    description = "Ultimas publicaciones de mi Blog"

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, obj):
        return obj.title
    
    def item_description(self, obj):
        return truncatewords_html(markdown.markdown(obj.body), 30)
    
    def item_pubdate(self ,obj):
        return obj.publish
    
    # item_link(self, obj) calls method of the get_absolute_url