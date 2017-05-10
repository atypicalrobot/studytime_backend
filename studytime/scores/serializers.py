from rest_framework import serializers

from .models import MultipleChoiceScore, TextScore, TrueOrFalseScore

# from studytime.questions.serializers import MultipleChoiceQuestionSerializer


class MultipleChoiceScoreSerializer(serializers.ModelSerializer):
    # question = MultipleChoiceQuestionSerializer()

    class Meta:
        # fields = ['id', 'name', 'question']
        fields = '__all__'
        model = MultipleChoiceScore


class TextScoreSerializer(serializers.ModelSerializer):
    # question = MultipleChoiceQuestionSerializer()

    class Meta:
        # fields = ['id', 'name', 'question']
        fields = '__all__'
        model = TextScore


class TrueOrFalseScoreSerializer(serializers.ModelSerializer):
    # question = MultipleChoiceQuestionSerializer()

    class Meta:
        # fields = ['id', 'name', 'question']
        fields = '__all__'
        model = TrueOrFalseScore
