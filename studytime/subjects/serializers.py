from rest_framework import serializers
from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Subject
