from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string

from applications.main.models import Preference


class Appointment(models.Model):
    """
    Запись на встречу
    """

    phone = models.CharField(
        verbose_name='Телефон',
        max_length=50,
    )

    name = models.CharField(
        verbose_name='Имя, фамилия',
        max_length=50,
        blank=True,
    )

    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True,
    )

    time = models.CharField(
        verbose_name='Время',
        max_length=50,
        blank=True,
    )

    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )

    class Meta:
        ordering = ['-created']
        verbose_name = 'запись'
        verbose_name_plural = 'запись на встречу'

    def clean(self):
        phone_list = [int(p) for p in str(self.phone) if p.isdigit()]
        if len(phone_list) != 12:
            raise ValidationError('Неверный номер телефона')

    def mail_admin(self):
        preference = Preference.objects.first()
        if preference:
            content = render_to_string(
                'capture/letters/mail_admin_appointment.html',
                {'object': self, 'preference': preference},
            )
            email_list = preference.email_appointment.split('\r\n')
            if email_list:
                msg = send_mail(
                    subject='SmartHome. Запись на встречу. #{}'.format(self.pk),
                    message=content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=email_list,
                    html_message=content,
                )
                return msg
        return False

    def __str__(self):
        return self.phone
