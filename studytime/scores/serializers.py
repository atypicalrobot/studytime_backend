from rest_framework import serializers

from .models import MultipleChoiceScore

# from studytime.questions.serializers import MultipleChoiceQuestionSerializer


class MultipleChoiceScoreSerializer(serializers.ModelSerializer):
    # questions = MultipleChoiceQuestionSerializer(many=True)

    class Meta:
        # fields = ['id', 'name', 'questions']
        fields = '__all__'
        model = MultipleChoiceScore
