from rest_framework import viewsets

from .models import MultipleChoiceQuiz, TextQuiz
from .serializers import MultipleChoiceQuizSerializer, TextQuizSerializer


class TextQuizViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    serializer_class = TextQuizSerializer
    queryset = TextQuiz.objects.all()


class MultipleChoiceQuizViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    serializer_class = MultipleChoiceQuizSerializer
    queryset = MultipleChoiceQuiz.objects.all()
