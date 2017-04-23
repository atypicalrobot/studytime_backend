from django.contrib import admin
from .models import Quiz, TextQuestion, MultipleChoiceQuestion, TrueOrFalseQuestion, TextAnswer, MultipleChoiceAnswer, TrueOrFalseAnswer


class TextQuestionInline(admin.TabularInline):
    model = TextQuestion


class TextAnswerInline(admin.TabularInline):
    model = TextAnswer


class MultipleChoiceAnswerInline(admin.TabularInline):
    model = MultipleChoiceAnswer


class TrueOrFalseAnswerInline(admin.TabularInline):
    model = TrueOrFalseAnswer


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [
        TextQuestionInline,
    ]


@admin.register(TextQuestion)
class TextQuestionAdmin(admin.ModelAdmin):
    inlines = [
        TextAnswerInline,
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

# @admin.register(TextAnswer)
# class TextAnswer(admin.ModelAdmin):
#     pass


# @admin.register(MultipleChoiceAnswer)
# class MultipleChoiceAnswer(admin.ModelAdmin):
#     pass


# @admin.register(TrueOrFalseAnswer)
# class TrueOrFalseAnswer(admin.ModelAdmin):
#     pass
