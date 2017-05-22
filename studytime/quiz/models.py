from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse

from studytime.subjects.models import Subject


@python_2_unicode_compatible
class Quiz(models.Model):

    name = models.CharField(max_length=60)
    subject = models.ForeignKey(Subject)
    # TODO: add level here.

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    @property
    def score(self):
        correct = self.questions.aggregate(models.Sum('score__correct'))['score__correct__sum']
        incorrect = self.questions.aggregate(models.Sum('score__incorrect'))['score__incorrect__sum']
        total_score = correct - incorrect
        if total_score < 0:
            total_score = 0
        return {
            'correct': correct,
            'incorrect': incorrect,
            'total_score': total_score
        }


# MultipleChoiceQuiz
@python_2_unicode_compatible
class TextQuiz(Quiz):
    pass


@python_2_unicode_compatible
class MultipleChoiceQuiz(Quiz):
    
    def get_absolute_url(self):
        return reverse('multiplechoicequiz-detail', kwargs={'pk': self.pk})


@python_2_unicode_compatible
class TrueOrFalseQuiz(Quiz):
    pass
