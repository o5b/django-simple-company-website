from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

from applications.core.admin import CommonAdmin

from . import models


@admin.register(models.Slide)
class SlideAdmin(SortableAdminMixin, CommonAdmin):
    list_display = ['title', 'thumb_photo', 'status']
    search_fields = ['title']


@admin.register(models.Index)
class IndexAdmin(SingleModelAdmin):
    pass


class AboutPhotoInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.AboutPhoto
    readonly_fields = ['thumb_photo']
    extra = 0


@admin.register(models.About)
class AboutAdmin(SingleModelAdmin):
    inlines = [AboutPhotoInline]


@admin.register(models.Page)
class PageAdmin(CommonAdmin):
    list_display = ['title', 'get_absolute_url', 'created', 'status']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ['title']}


@admin.register(models.Preference)
class PreferenceAdmin(SingleModelAdmin):
    pass
