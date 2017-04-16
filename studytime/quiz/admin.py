from django.contrib import admin
from .models import Quiz, Question, MultipleChoiceQuestion, TrueOrFalseQuestion, Answer, MultipleChoiceAnswer, TrueOrFalseAnswer


class QuestionInline(admin.TabularInline):
    model = Question


class AnswerInline(admin.TabularInline):
    model = Answer


class MultipleChoiceAnswerInline(admin.TabularInline):
    model = MultipleChoiceAnswer


class TrueOrFalseAnswerInline(admin.TabularInline):
    model = TrueOrFalseAnswer


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]


@admin.register(MultipleChoiceQuestion)
class MultipleChoiceQuestionAdmin(admin.ModelAdmin):
    inlines = [
        MultipleChoiceAnswerInline,
    ]


@admin.register(TrueOrFalseQuestion)
class TrueOrFalseQuestionAdmin(admin.ModelAdmin):
    inlines = [
        TrueOrFalseAnswerInline,
    ]

@admin.register(Answer)
class Answer(admin.ModelAdmin):
    pass


@admin.register(MultipleChoiceAnswer)
class MultipleChoiceAnswer(admin.ModelAdmin):
    pass


@admin.register(TrueOrFalseAnswer)
class TrueOrFalseAnswer(admin.ModelAdmin):
    pass
