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
class Question(models.Model):

    prompt_text = models.CharField(max_length=250)
    reprompt_text = models.CharField(max_length=250, blank=True)
    quiz = models.ForeignKey(Quiz)


    class Meta:
        abstract = True


    @property
    def prompt(self):
        return self.prompt_text

    @property
    def reprompt(self):
        return self.reprompt_text

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

    @property 
    def prompt(self):
        return self.prompt_text


@python_2_unicode_compatible
class MultipleChoiceQuestion(Question):
    """docstring for ClassName"""

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

    answers = ArrayField(
        models.CharField(max_length=250),
    )

    class Meta:
        abstract = True

    @property
    def answer(self):
        raise NotImplementedError('You need to implement answer on an answer')

    def __str__(self):
        return 'Question: {} Answer: {}'.format(self.question, self.answer)


@python_2_unicode_compatible
class TextAnswer(Answer):

    question = models.OneToOneField(TextQuestion)

    @property
    def answer(self):
        return self.answers[0]


@python_2_unicode_compatible
class MultipleChoiceAnswer(Answer):

    question = models.OneToOneField(MultipleChoiceQuestion)

    choices = ArrayField(
        models.CharField(max_length=250),
    )

    @property
    def answer(self):
        # Make sure choices contains the answer!
        return self.answers


@python_2_unicode_compatible
class TrueOrFalseAnswer(Answer):

    question = models.OneToOneField(TrueOrFalseQuestion)

    @property
    def answer(self):
        return bool(self.answers[0])
