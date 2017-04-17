from django.shortcuts import render
from rest_framework import viewsets

from .models import Quiz
from .serializers import QuizSerializer


class QuizViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
