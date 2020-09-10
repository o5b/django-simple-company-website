from django.http import Http404
from django.urls import path
from multiurl import ContinueResolving, multiurl

from applications.main.views import PageDetailView

from . import views

urlpatterns = [
    path(
        'price/',
        views.PriceListView.as_view(),
        name='price_list',
    ),
    multiurl(
        path(
            '<str:slug>/',
            PageDetailView.as_view(),
            name='page_detail',
        ),
        path(
            '<str:slug>/',
            views.ServiceDetailView.as_view(),
            name='service_detail',
        ),
        catch=(
            Http404,
            ContinueResolving,
        ),
    ),
]
