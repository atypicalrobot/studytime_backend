from rest_framework import mixins, viewsets

from .filters import MultipleChoiceQuizFilter
from .models import MultipleChoiceQuiz, TextQuiz, TrueOrFalseQuiz
from .serializers import MultipleChoiceQuizSerializer, TextQuizSerializer, TrueOrFalseQuizSerializer


class TextQuizViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    serializer_class = TextQuizSerializer
    queryset = TextQuiz.objects.all()


class MultipleChoiceQuizViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    serializer_class = MultipleChoiceQuizSerializer
    filter_class = MultipleChoiceQuizFilter
    queryset = MultipleChoiceQuiz.objects.all()


class TrueOrFalseQuizViewSet(mixins.CreateModelMixin,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    serializer_class = TrueOrFalseQuizSerializer
    queryset = TrueOrFalseQuiz.objects.all()
