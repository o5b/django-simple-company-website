from django.contrib import admin
from . import models


@admin.register(models.Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['phone', 'name', 'time', 'comment', 'created']
    readonly_fields = ['created']
    search_fields = ['name', 'phone']
    date_hierarchy = 'created'
