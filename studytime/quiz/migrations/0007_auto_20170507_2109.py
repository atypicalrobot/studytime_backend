# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-07 21:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20170423_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multiplechoiceanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='multiplechoicequestion',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='textanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='textquestion',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='trueorfalseanswer',
            name='question',
        ),
        migrations.DeleteModel(
            name='MultipleChoiceAnswer',
        ),
        migrations.DeleteModel(
            name='MultipleChoiceQuestion',
        ),
        migrations.DeleteModel(
            name='TextAnswer',
        ),
        migrations.DeleteModel(
            name='TextQuestion',
        ),
        migrations.DeleteModel(
            name='TrueOrFalseAnswer',
        ),
        migrations.DeleteModel(
            name='TrueOrFalseQuestion',
        ),
    ]
