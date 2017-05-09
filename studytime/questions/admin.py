from django.contrib import admin

from .models import TextQuestion, MultipleChoiceQuestion, TrueOrFalseQuestion, TextAnswer, MultipleChoiceAnswer, TrueOrFalseAnswer


class TextAnswerInline(admin.TabularInline):
    model = TextAnswer


class MultipleChoiceAnswerInline(admin.TabularInline):
    model = MultipleChoiceAnswer


class TrueOrFalseAnswerInline(admin.TabularInline):
    model = TrueOrFalseAnswer


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
