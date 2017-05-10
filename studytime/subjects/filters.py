import rest_framework_filters as filters

from .models import Subject


class SubjectFilter(filters.FilterSet):
    class Meta:
        model = Subject
        fields = {'name': ['exact']}
