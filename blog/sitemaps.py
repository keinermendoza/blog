from django.contrib.sitemaps import Sitemap
from blog.models import Post

class PostSitemap(Sitemap):
    changefreq = "hourly"
    priority = 1
    # protocol = "https"

    def items(self):
        return Post.published.all()
    
    def lastmod(self, obj):
        return obj.updated
    