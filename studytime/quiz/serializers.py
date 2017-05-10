from rest_framework import serializers

from .models import MultipleChoiceQuiz, TextQuiz, TrueOrFalseQuiz

from studytime.questions.serializers import MultipleChoiceQuestionSerializer


class TextQuizSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TextQuiz


class MultipleChoiceQuizSerializer(serializers.ModelSerializer):
    questions = MultipleChoiceQuestionSerializer(many=True)

    class Meta:
        fields = ['id', 'name', 'questions']
        # fields = '__all__'
        model = MultipleChoiceQuiz


class TrueOrFalseQuizSerializer(serializers.ModelSerializer):
    questions = MultipleChoiceQuestionSerializer(many=True)

    class Meta:
        fields = ['id', 'name', 'questions']
        # fields = '__all__'
        model = TrueOrFalseQuiz
