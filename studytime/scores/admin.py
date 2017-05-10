from django.contrib import admin

from .models import MultipleChoiceScore, TextScore, TrueOrFalseScore


@admin.register(MultipleChoiceScore)
class MultipleChoiceScore(admin.ModelAdmin):
    pass


@admin.register(TextScore)
class TextScore(admin.ModelAdmin):
    pass


@admin.register(TrueOrFalseScore)
class TrueOrFalseScore(admin.ModelAdmin):
    pass
