from rest_framework import serializers

from .models import MultipleChoiceAnswer, MultipleChoiceQuestion, TextQuestion, TextAnswer, TrueOrFalseAnswer, TrueOrFalseQuestion


class MultipleChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'choices', 'question', 'answers']
        model = MultipleChoiceAnswer


class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    answer = MultipleChoiceAnswerSerializer()

    class Meta:
        fields = ['id', 'prompt_text', 'reprompt', 'answer']
        model = MultipleChoiceQuestion


class TextAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'question', 'answers']
        model = TextAnswer


class TextQuestionSerializer(serializers.ModelSerializer):
    answer = TextAnswerSerializer()

    class Meta:
        fields = ['id', 'prompt_text', 'reprompt', 'answer']
        model = TextQuestion


class TrueOrFalseAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'question', 'answers']
        model = TrueOrFalseAnswer


class TrueOrFalseQuestionSerializer(serializers.ModelSerializer):
    answer = TrueOrFalseAnswerSerializer()

    class Meta:
        fields = ['id', 'prompt_text', 'reprompt', 'answer']
        model = TrueOrFalseQuestion
