# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from rest_framework import mixins, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from studytime.scores.models import MultipleChoiceScore, TextScore, TrueOrFalseScore

from .models import MultipleChoiceQuestion, TextQuestion, TrueOrFalseQuestion
from .serializers import MultipleChoiceQuestionSerializer, TextQuestionSerializer, TrueOrFalseQuestionSerializer


class MultipleChoiceQuestionViewSet(mixins.CreateModelMixin,
                                    mixins.ListModelMixin,
                                    mixins.RetrieveModelMixin,
                                    viewsets.GenericViewSet):
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
        score = MultipleChoiceScore.object.get(
            question=question.pk, user=request.user)
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


class TextQuestionViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    serializer_class = TextQuestionSerializer
    queryset = TextQuestion.objects.all()

    @detail_route(methods=['post'])
    def correct(self, request, pk=None):
        """
        A view to track a correct answer for question and current user.
        """
        question = self.get_object()
        score = TextScore.object.get(question=question.pk, user=request.user)
        score.correct += 1
        score.save()
        return Response({'status': 'ok'})

    @detail_route(methods=['post'])
    def incorrect(self, request, pk=None):
        """
        A view to track an incorrect answer for question and current user.
        """
        score = TextScore.object.get(question=pk, user=request.user)
        score.incorrect += 1
        score.save()
        return Response({'status': 'ok'})


class TrueOrFalseQuestionViewSet(mixins.CreateModelMixin,
                                 mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin,
                                 viewsets.GenericViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    serializer_class = TrueOrFalseQuestionSerializer
    queryset = TrueOrFalseQuestion.objects.all()

    @detail_route(methods=['post'])
    def correct(self, request, pk=None):
        """
        A view to track a correct answer for question and current user.
        """
        question = self.get_object()
        score = TrueOrFalseScore.object.get(
            question=question.pk, user=request.user)
        score.correct += 1
        score.save()
        return Response({'status': 'ok'})

    @detail_route(methods=['post'])
    def incorrect(self, request, pk=None):
        """
        A view to track an incorrect answer for question and current user.
        """
        score = TrueOrFalseScore.object.get(question=pk, user=request.user)
        score.incorrect += 1
        score.save()
        return Response({'status': 'ok'})


# Frontend Views

class MultipleChoiceQuestionDetailView(LoginRequiredMixin, DetailView):
    model = MultipleChoiceQuestion
    # These next two lines tell the view to index lookups by username
    slug_field = 'id'
    slug_url_kwarg = 'id'


class MultipleChoiceQuestionRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class MultipleChoiceQuestionUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['id', ]

    # we already imported User in the view code above, remember?
    model = MultipleChoiceQuestion

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('questions:detail',
                       kwargs={'id': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return MultipleChoiceQuestion.objects.get(username=self.request.user.username)


class MultipleChoiceQuestionListView(LoginRequiredMixin, ListView):
    model = MultipleChoiceQuestion
    # These next two lines tell the view to index lookups by username
    slug_field = 'id'
    slug_url_kwarg = 'id'
