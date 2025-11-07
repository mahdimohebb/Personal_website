from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Portfolio


class StaticViewSitemap(Sitemap):
    """Sitemap برای صفحات استاتیک"""
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['main:home_page']

    def location(self, item):
        return reverse(item)


class PortfolioSitemap(Sitemap):
    """Sitemap برای نمونه کارها"""
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Portfolio.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at

