from haystack import indexes
from . import models


class ServiceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title', boost=1.125)
    content = indexes.CharField(model_attr='content')
    created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return models.Service

    def index_queryset(self, using=None):
        return self.get_model().published.all()
