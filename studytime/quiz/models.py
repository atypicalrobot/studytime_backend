from django.contrib.postgres.fields import ArrayField
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


@python_2_unicode_compatible
class QuestionBase(models.Model):

    prompt_text = models.CharField(max_length=250)
    reprompt_text = models.CharField(max_length=250, blank=True)
    quiz = models.ForeignKey(Quiz)

    class Meta:
        abstract = True

    @property
    def prompt(self):
        raise NotImplementedError('You need to implement prompt on a question')

    # @property
    # def reprompt(self):
    #     raise NotImplementedError('You need to implement reprompt on a question')

    @property
    def reprompt(self):
        if self.reprompt_text:
            return self.reprompt_text
        else:
            return self.prompt

    def __str__(self):
        return self.prompt


@python_2_unicode_compatible
class Question(QuestionBase):

    @property
    def prompt(self):
        return self.prompt_text


@python_2_unicode_compatible
class MultipleChoiceQuestion(QuestionBase):
    """docstring for ClassName"""
    choices = ArrayField(
        models.CharField(max_length=250),
    )

    @property
    def prompt(self):
        return '{} {}'.format(self.prompt_text, self.choices)


@python_2_unicode_compatible
class TrueOrFalseQuestion(QuestionBase):
    """docstring for ClassName"""

    @property
    def prompt(self):
        return '{} {}'.format(self.prompt_text, 'true or false?')


@python_2_unicode_compatible
class AnswerBase(models.Model):

    @property
    def answer(self):
        raise NotImplementedError('You need to implement answer on an answer')

    class Meta:
        abstract = True

    def __str__(self):
        return 'Question: {} Answer: {}'.format(self.question, self.answer)


@python_2_unicode_compatible
class Answer(AnswerBase):

    question = models.OneToOneField(Question)
    answer_text = models.CharField(max_length=250)

    @property
    def answer(self):
        return self.answer_text


@python_2_unicode_compatible
class MultipleChoiceAnswer(AnswerBase):

    question = models.OneToOneField(MultipleChoiceQuestion)

    answers = ArrayField(
        models.CharField(max_length=250),
    )

    @property
    def answer(self):
        return self.answers


@python_2_unicode_compatible
class TrueOrFalseAnswer(AnswerBase):

    question = models.OneToOneField(TrueOrFalseQuestion)

    answer_bool = models.BooleanField()

    @property
    def answer(self):
        return self.answer_bool

