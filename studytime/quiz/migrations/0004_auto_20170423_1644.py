# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20170423_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiplechoicequestion',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='quiz.MultipleChoiceQuiz'),
        ),
    ]
