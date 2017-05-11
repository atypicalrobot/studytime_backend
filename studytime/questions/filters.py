import rest_framework_filters as filters

from .models import MultipleChoiceQuestion


class MultipleChoiceQuestionFilter(filters.FilterSet):
    class Meta:
        model = MultipleChoiceQuestion
        fields = {'prompt_text': ['exact', 'in', 'startswith']}
