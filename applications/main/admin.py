from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from singlemodeladmin import SingleModelAdmin

from applications.core.admin import CommonAdmin

from . import models


@admin.register(models.Slide)
class SlideAdmin(SortableAdminMixin, CommonAdmin, TabbedTranslationAdmin):
    list_display = ['title', 'thumb_photo', 'status']
    search_fields = ['title']


@admin.register(models.Index)
class IndexAdmin(SingleModelAdmin, TabbedTranslationAdmin):
    pass


class AboutPhotoInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.AboutPhoto
    readonly_fields = ['thumb_photo']
    extra = 0


@admin.register(models.About)
class AboutAdmin(SingleModelAdmin, TabbedTranslationAdmin):
    inlines = [AboutPhotoInline]


@admin.register(models.Page)
class PageAdmin(CommonAdmin, TabbedTranslationAdmin):
    list_display = ['title', 'get_absolute_url', 'created', 'status']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ['title']}


@admin.register(models.Preference)
class PreferenceAdmin(SingleModelAdmin, TabbedTranslationAdmin):
    pass


@admin.register(models.IndexVideo)
class IndexVideoAdmin(SortableAdminMixin, CommonAdmin):
    list_display = ['thumb_photo', 'status']
    search_fields = ['youtube_link']
    filter_horizontal = ['services']
