from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, UpdateView
from rest_framework import mixins, viewsets

from .filters import MultipleChoiceQuizFilter
from .forms import MultipleChoiceQuizForm
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


# Frontend Views
class MultipleChoiceQuizDetailView(LoginRequiredMixin, DetailView):
    model = MultipleChoiceQuiz
    # These next two lines tell the view to index lookups by ID
    slug_field = 'id'
    slug_url_kwarg = 'id'


class MultipleChoiceQuizUpdateView(LoginRequiredMixin, UpdateView):

    form_class = MultipleChoiceQuizForm

    model = MultipleChoiceQuiz

    # send the user back to their own page after a successful update
    def get_success_url(self):
        print(self)
        print(dir(self))
        return self.get_object().get_absolute_url()


class MultipleChoiceQuizListView(LoginRequiredMixin, ListView):
    model = MultipleChoiceQuiz
    # These next two lines tell the view to index lookups by ID
    slug_field = 'id'
    slug_url_kwarg = 'id'
