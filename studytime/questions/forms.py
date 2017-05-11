from django import forms

from .models import MultipleChoiceQuestion, MultipleChoiceAnswer
from .fields import ArrayFieldWidget


class MultipleChoiceQuestionForm(forms.ModelForm):

    class Meta:
        model = MultipleChoiceQuestion
        fields = ['quiz', 'prompt_text', 'reprompt_text']


class MultipleChoiceAnswerForm(forms.ModelForm):

    class Meta:
        model = MultipleChoiceAnswer
        fields = ['choices', 'answer_array']
        widgets = {
            # 'answer_array': ArrayFieldWidget
        }
