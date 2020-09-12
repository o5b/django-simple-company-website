from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from django.contrib.sitemaps.views import sitemap

from applications.core.sitemap import (SitemapWeekly, SitemapDaily)
sitemaps = {'weekly': SitemapWeekly, 'daily': SitemapDaily}


urlpatterns = [
    path(
        'sitemap.xml/',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),

    path(
        'admin/',
        admin.site.urls,
    ),

    path(
        'admin/rosetta/',
        include('rosetta.urls'),
    ),

    path(
        'ckeditor/',
        include('ckeditor_uploader.urls'),
    ),
]

urlpatterns += i18n_patterns(
    path(
        'capture/',
        include(('applications.capture.urls', 'capture'), namespace='capture'),
    ),

    path(
        'search/',
        include('haystack.urls'),
    ),

    path(
        '',
        include(('applications.main.urls', 'main'), namespace='main'),
    ),

    path(
        '',
        include(('applications.services.urls', 'services'), namespace='services'),
    ),

    prefix_default_language=False
)

urlpatterns += staticfiles_urlpatterns() + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
