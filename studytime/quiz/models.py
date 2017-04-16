from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from studytime.subjects.models import Subject


@python_2_unicode_compatible
class Quiz(models.Model):

    name = models.CharField(max_length=60)
    subject = models.ForeignKey(Subject)
    # TODO: add level here.


    def __str__(self):
        return self.name


class Question(models.Model):

    prompt = models.CharField(max_length=250)
    reprompt = models.CharField(max_length=250)
    quiz = models.ForeignKey(Quiz)
    answer = models.CharField(max_length=250)


    def __str__(self):
        return self.prompt
