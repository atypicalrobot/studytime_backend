from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from studytime.quiz.models import MultipleChoiceQuiz, TextQuiz


@python_2_unicode_compatible
class Question(models.Model):

    prompt_text = models.CharField(max_length=250)
    reprompt_text = models.CharField(max_length=250, blank=True)

    class Meta:
        abstract = True

    @property
    def prompt(self):
        return self.prompt_text

    @property
    def reprompt(self):
        if self.reprompt_text:
            return self.reprompt_text
        else:
            return self.prompt

    def __str__(self):
        return self.prompt


@python_2_unicode_compatible
class TextQuestion(Question):

    quiz = models.ForeignKey(TextQuiz)

    @property
    def prompt(self):
        return self.prompt_text


@python_2_unicode_compatible
class MultipleChoiceQuestion(Question):
    """docstring for ClassName"""

    quiz = models.ForeignKey(MultipleChoiceQuiz, related_name='questions')

    @property
    def choices(self):
        return self.answer.choices

    @property
    def prompt(self):
        return '{} {}'.format(self.prompt_text, self.choices)


@python_2_unicode_compatible
class TrueOrFalseQuestion(Question):
    """docstring for ClassName"""

    @property
    def prompt(self):
        return '{} {}'.format(self.prompt_text, 'true or false?')


@python_2_unicode_compatible
class Answer(models.Model):

    class Meta:
        abstract = True

    @property
    def answers(self):
        raise NotImplementedError('You need to implement answers (plural) on an answer')

    @property
    def answer(self):
        raise NotImplementedError('You need to implement answer (singular) on an answer')

    def __str__(self):
        return 'Question: {} Answer: {}'.format(self.question, self.answers)


@python_2_unicode_compatible
class TextAnswer(Answer):

    question = models.OneToOneField(TextQuestion)
    answer_array = ArrayField(
        models.CharField(max_length=250),
    )

    @property
    def answers(self):
        return self.answer_array

    @property
    def answer(self):
        return self.answer_array


@python_2_unicode_compatible
class MultipleChoiceAnswer(Answer):

    question = models.OneToOneField(MultipleChoiceQuestion, related_name='answer')

    choices = ArrayField(
        models.CharField(max_length=250),
    )

    ANSWER_CHOICES = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    )
    answer_array = ArrayField(models.CharField(
        max_length=1, choices=ANSWER_CHOICES), default=[], blank=True, null=True, help_text='e.g. a,b,c'
    )

    @property
    def answers(self):
        return self.answer_array

    @property
    def answer(self):
        return self.answer_array


@python_2_unicode_compatible
class TrueOrFalseAnswer(Answer):

    question = models.OneToOneField(TrueOrFalseQuestion)
    answer_singular = models.BooleanField()

    @property
    def answers(self):
        # avoid getting a NotImplementedError
        return self.answer_singular

    @property
    def answer(self):
        return self.answer_singular
