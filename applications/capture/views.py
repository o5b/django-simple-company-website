from django.http import JsonResponse
from django.views.generic import CreateView

from . import models


class AjaxFormMixin():
    def get(self, *args, **kwargs):
        return JsonResponse({}, status=400)

    def mail_object(self):
        raise NotImplementedError

    def form_valid(self, form):
        self.object = form.save()
        self.mail_object()
        return JsonResponse({})

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)


class AppointmentCreateView(AjaxFormMixin, CreateView):
    model = models.Appointment
    fields = [
        'phone',
        'time',
        'name',
        'comment',
    ]

    def mail_object(self):
        self.object.mail_admin()
