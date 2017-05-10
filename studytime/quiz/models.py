from django.db import models
from django.utils.encoding import python_2_unicode_compatible

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


# MultipleChoiceQuiz
@python_2_unicode_compatible
class TextQuiz(Quiz):
    pass


@python_2_unicode_compatible
class MultipleChoiceQuiz(Quiz):
    pass


@python_2_unicode_compatible
class TrueOrFalseQuiz(Quiz):
    pass
