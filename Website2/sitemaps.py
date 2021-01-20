from django.contrib.sitemaps import Sitemap
from .models import PostPage

class PostSitemap(Sitemap):
    changefreq='never'
    priority=0.5

    def items(self):
        return PostPage.objects.all()