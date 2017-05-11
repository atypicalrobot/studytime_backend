from rest_framework import mixins, viewsets

from .models import MultipleChoiceScore, TextScore, TrueOrFalseScore
from .serializers import MultipleChoiceScoreSerializer, TextScoreSerializer, TrueOrFalseScoreSerializer


class MultipleChoiceScoreViewSet(mixins.CreateModelMixin,
                                 mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin,
                                 viewsets.GenericViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    serializer_class = MultipleChoiceScoreSerializer
    queryset = MultipleChoiceScore.objects.all()


class TextScoreViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    serializer_class = TextScoreSerializer
    queryset = TextScore.objects.all()


class TrueOrFalseScoreViewSet(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    serializer_class = TrueOrFalseScoreSerializer
    queryset = TrueOrFalseScore.objects.all()
