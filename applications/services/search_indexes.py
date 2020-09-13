from haystack import indexes
from . import models


class ServiceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title_ru = indexes.CharField(model_attr='title_ru', boost=1.125)
    title_en = indexes.CharField(model_attr='title_en', boost=1.125, null=True)
    content_ru = indexes.CharField(model_attr='content_ru')
    content_en = indexes.CharField(model_attr='content_en', null=True)
    created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return models.Service

    def index_queryset(self, using=None):
        return self.get_model().published.all()
