from haystack import indexes
from . import models


class AboutIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    comment = indexes.CharField(model_attr='comment', boost=1.125)
    content_1 = indexes.CharField(model_attr='content_1')
    content_2 = indexes.CharField(model_attr='content_2')

    def get_model(self):
        return models.About

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class PageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title', boost=1.125)
    content = indexes.CharField(model_attr='content')
    created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return models.Page

    def index_queryset(self, using=None):
        return self.get_model().published.all()
