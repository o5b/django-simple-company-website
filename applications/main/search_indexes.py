from haystack import indexes
from . import models


class AboutIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    comment_ru = indexes.CharField(model_attr='comment_ru', boost=1.125)
    comment_en = indexes.CharField(model_attr='comment_en', boost=1.125, null=True)
    content_1_ru = indexes.CharField(model_attr='content_1_ru')
    content_1_en = indexes.CharField(model_attr='content_1_en', null=True)
    content_2_ru = indexes.CharField(model_attr='content_2_ru')
    content_2_en = indexes.CharField(model_attr='content_2_en', null=True)

    def get_model(self):
        return models.About

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class PageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title_ru = indexes.CharField(model_attr='title_ru', boost=1.125)
    title_en = indexes.CharField(model_attr='title_en', boost=1.125, null=True)
    content_ru = indexes.CharField(model_attr='content_ru')
    content_en = indexes.CharField(model_attr='content_en', null=True)
    created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return models.Page

    def index_queryset(self, using=None):
        return self.get_model().published.all()


class IndexIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    content_1_ru = indexes.CharField(model_attr='content_1_ru')
    content_1_en = indexes.CharField(model_attr='content_1_en', null=True)
    content_2_ru = indexes.CharField(model_attr='content_2_ru')
    content_2_en = indexes.CharField(model_attr='content_2_en', null=True)

    def get_model(self):
        return models.Index

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
