from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from studytime.scores.models import MultipleChoiceScore

from .models import MultipleChoiceQuestion
from .serializers import MultipleChoiceQuestionSerializer


class MultipleChoiceQuestionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    serializer_class = MultipleChoiceQuestionSerializer
    queryset = MultipleChoiceQuestion.objects.all()

    @detail_route(methods=['post'])
    def correct(self, request, pk=None):
        """
        A view to track a correct answer for question and current user.
        """
        question = self.get_object()
        score = MultipleChoiceScore.object.get(question=question.pk, user=request.user)
        score.correct += 1
        score.save()
        return Response({'status': 'ok'})

    @detail_route(methods=['post'])
    def incorrect(self, request, pk=None):
        """
        A view to track an incorrect answer for question and current user.
        """
        score = MultipleChoiceScore.object.get(question=pk, user=request.user)
        score.incorrect += 1
        score.save()
        return Response({'status': 'ok'})
