from rest_framework import viewsets

from .models import MultipleChoiceQuestion
from .serializers import MultipleChoiceQuestionSerializer


class MultipleChoiceQuestionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    serializer_class = MultipleChoiceQuestionSerializer
    queryset = MultipleChoiceQuestion.objects.all()
