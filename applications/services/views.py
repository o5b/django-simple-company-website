from django.views.generic import DetailView, ListView

from . import models


class ServiceDetailView(DetailView):
    template_name = 'services/service_detail.html'
    model = models.Service
    queryset = model.published.all()


class PriceListView(ListView):
    template_name = 'services/price_list.html'
    model = models.Service
    queryset = model.objects.all()
