from __future__ import absolute_import, unicode_literals

from django.conf import settings
# from celery import task
from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string

from . import models
from applications.main.models import Preference


# @task
@shared_task
def appointment_created(appointment_id):
    """
    Task to send an e-mail notification when an appointment is
    successfully created.
    """
    appointment = models.Appointment.objects.get(id=appointment_id)
    preference = Preference.objects.first() or {}
    if preference:
        content = render_to_string(
            'capture/letters/mail_admin_appointment.html',
            {'object': appointment, 'preference': preference},
        )
        email_list = preference.email_appointment.split('\r\n')
        if email_list:
            msg = send_mail(
                subject='SmartHome. Запись на встречу. #{}'.format(appointment.pk),
                message=content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=email_list,
                html_message=content,
            )
            return msg
    return False
