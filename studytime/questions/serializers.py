from rest_framework import serializers

from studytime.scores.models import MultipleChoiceScore

from .models import MultipleChoiceAnswer, MultipleChoiceQuestion, TextQuestion, TextAnswer, TrueOrFalseAnswer, TrueOrFalseQuestion


class MultipleChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'choices', 'question', 'answers']
        model = MultipleChoiceAnswer


class MultipleChoiceScoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['correct', 'incorrect', 'total_score']
        model = MultipleChoiceScore


class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    answer = MultipleChoiceAnswerSerializer()
    score = MultipleChoiceScoreSerializer()

    class Meta:
        fields = ['id', 'prompt_text', 'reprompt', 'answer', 'score']
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
