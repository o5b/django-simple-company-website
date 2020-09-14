from django_object_actions import DjangoObjectActions

from django.conf import settings
from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string

from applications.main.models import Preference
from . import models


@admin.register(models.Appointment)
class AppointmentAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ['phone', 'name', 'time', 'comment', 'created']
    readonly_fields = ['created']
    search_fields = ['name', 'phone']
    date_hierarchy = 'created'
    change_actions = ['appointment_mail']

    def appointment_mail(self, request, obj):
        preference = Preference.objects.first() or {}
        if preference:
            content = render_to_string(
                'capture/letters/mail_admin_appointment.html',
                {'object': obj, 'preference': preference},
            )
            email_list = preference.email_appointment.split('\r\n')
            if email_list:
                msg = send_mail(
                    subject='SmartHome. Запись на встречу. #{}'.format(obj.pk),
                    message=content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=email_list,
                    html_message=content,
                )
                return msg
        return False
    appointment_mail.label = 'Отправить уведомление на email'
    appointment_mail.short_description = 'Повторно отправить email о записи на прием'
