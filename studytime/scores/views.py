from rest_framework import viewsets

from .models import MultipleChoiceScore
from .serializers import MultipleChoiceScoreSerializer


class MultipleChoiceScoreViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    serializer_class = MultipleChoiceScoreSerializer
    queryset = MultipleChoiceScore.objects.all()
