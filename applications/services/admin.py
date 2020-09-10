from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from django.contrib import admin

from applications.core.admin import CommonAdmin
from . import models


class MediaInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.Media
    readonly_fields = ['thumb_photo']
    extra = 0


class PriceInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.Price
    extra = 0


@admin.register(models.Service)
class ServiceAdmin(CommonAdmin):
    list_display = ['title', 'status']
    list_filter = ['status',]
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ['title']}
    inlines = [MediaInline, PriceInline]


@admin.register(models.Price)
class PriceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'service', 'price']
    search_fields = ['title', 'service__title', 'price']


@admin.register(models.Popular)
class PopularAdmin(SortableAdminMixin, CommonAdmin):
    list_display = ['title', 'thumb_photo', 'status']
    list_filter = ['status']
    search_fields = ['title', 'description']
