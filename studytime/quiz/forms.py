from django import forms

from .models import MultipleChoiceQuiz


class MultipleChoiceQuizForm(forms.ModelForm):

    class Meta:
        model = MultipleChoiceQuiz
        fields = ['name', 'subject']
