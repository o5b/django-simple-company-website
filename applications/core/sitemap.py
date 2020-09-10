from django.contrib.sitemaps import Sitemap
from itertools import chain
from django.urls import reverse

from applications.main.models import Page
from applications.services.models import Service


class SitemapDaily(Sitemap):
    changefreq = 'weekly'
    priority = 1

    def items(self):
        return [
            'main:index',
            'main:about',
            'services:price_list',
        ]

    def location(self, item):
        return reverse(item)


class SitemapWeekly(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return list(
            chain(
                Page.published.all(),
                Service.published.all(),
            )
        )

    def lastmod(self, obj):
        return obj.created
