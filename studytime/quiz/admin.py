from django.contrib import admin

from .models import MultipleChoiceQuiz, TextQuiz, TrueOrFalseQuiz


@admin.register(TextQuiz)
class TextQuizAdmin(admin.ModelAdmin):
    pass


@admin.register(MultipleChoiceQuiz)
class MultipleChoiceQuizAdmin(admin.ModelAdmin):
    pass


@admin.register(TrueOrFalseQuiz)
class TrueOrFalseQuizAdmin(admin.ModelAdmin):
    pass
