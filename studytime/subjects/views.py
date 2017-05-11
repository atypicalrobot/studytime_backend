from rest_framework import mixins, viewsets

from .filters import SubjectFilter
from .models import Subject
from .serializers import SubjectSerializer


class SubjectViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    A viewset for viewing and editing subject instances.
    """
    serializer_class = SubjectSerializer
    filter_class = SubjectFilter
    queryset = Subject.objects.all()
