from django.urls import path
from . import views

urlpatterns = [
    path(
        'ajax/appointment/',
        views.AppointmentCreateView.as_view(),
        name='appointment_create',
    ),
]
