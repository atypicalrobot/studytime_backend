from django.contrib import admin

from .models import MultipleChoiceScore


@admin.register(MultipleChoiceScore)
class MultipleChoiceScore(admin.ModelAdmin):
    pass
