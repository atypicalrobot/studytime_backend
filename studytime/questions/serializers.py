from rest_framework import serializers

from .models import MultipleChoiceAnswer, MultipleChoiceQuestion


class MultipleChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = MultipleChoiceAnswer


class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    answer = MultipleChoiceAnswerSerializer()

    class Meta:
        fields = ['id', 'prompt_text', 'reprompt', 'answer']
        model = MultipleChoiceQuestion
