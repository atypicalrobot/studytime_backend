from django.db import models

from studytime.questions.models import MultipleChoiceQuestion
from studytime.users.models import User


class MultipleChoiceScore(models.Model):
    user = models.ForeignKey(User, related_name='multiple_choice_score')
    question = models.ForeignKey(MultipleChoiceQuestion, related_name='score')
    correct = models.IntegerField(default=0)
    incorrect = models.IntegerField(default=0)
