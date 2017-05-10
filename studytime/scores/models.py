from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from studytime.questions.models import MultipleChoiceQuestion, TextQuestion, TrueOrFalseQuestion
from studytime.users.models import User


@python_2_unicode_compatible
class Score(models.Model):
    correct = models.IntegerField(default=0)
    incorrect = models.IntegerField(default=0)

    class Meta:
        abstract = True

    @property
    def total_score(self):
        score = self.correct - self.incorrect
        if score < 0:
            score = 0
        return score

    def __str__(self):
        return 'Question: {} User: {} Score: {}'.format(self.question.prompt_text, self.user.username, self.total_score)


class MultipleChoiceScore(Score):
    user = models.ForeignKey(User, related_name='multiple_choice_score')
    question = models.ForeignKey(MultipleChoiceQuestion, related_name='score')


class TextScore(Score):
    user = models.ForeignKey(User, related_name='text_score')
    question = models.ForeignKey(TextQuestion, related_name='score')


class TrueOrFalseScore(Score):
    user = models.ForeignKey(User, related_name='true_or_false_score')
    question = models.ForeignKey(TrueOrFalseQuestion, related_name='score')
