from django_object_actions import DjangoObjectActions

from django.conf import settings
from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string

from applications.main.models import Preference
from . import models
from . tasks import appointment_created


@admin.register(models.Appointment)
class AppointmentAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ['phone', 'name', 'time', 'comment', 'created']
    readonly_fields = ['created']
    search_fields = ['name', 'phone']
    date_hierarchy = 'created'
    change_actions = ['mail_appointment']

    def mail_appointment(self, request, obj):
        appointment_created.delay(obj.pk)
    mail_appointment.label = 'Отправить уведомление на email'
    mail_appointment.short_description = 'Повторно отправить email о записи на прием'
