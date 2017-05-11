import rest_framework_filters as filters

from studytime.subjects.filters import SubjectFilter
from studytime.subjects.models import Subject

from .models import MultipleChoiceQuiz


class MultipleChoiceQuizFilter(filters.FilterSet):
    subject = filters.RelatedFilter(SubjectFilter, name='subject', queryset=Subject.objects.all())

    class Meta:
        model = MultipleChoiceQuiz
        fields = {
            'name': ['exact', 'in', 'startswith']
        }
