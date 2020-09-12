from modeltranslation.translator import TranslationOptions, register

from . import models


@register(models.Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = [
        'title',
        'content',
        'conclusion',
    ]


@register(models.Price)
class PriceTranslationOptions(TranslationOptions):
    fields = [
        'title',
        'price',
    ]


@register(models.Popular)
class PopularTranslationOptions(TranslationOptions):
    fields = [
        'title',
        'description',
    ]
