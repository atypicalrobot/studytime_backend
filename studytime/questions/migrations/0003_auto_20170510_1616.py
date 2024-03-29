# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 16:16
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import studytime.questions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20170510_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplechoiceanswer',
            name='flags',
            field=studytime.questions.fields.ChoiceArrayField(base_field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], max_length=1), default=['a'], size=None),
        ),
        migrations.AlterField(
            model_name='multiplechoiceanswer',
            name='answer_array',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]), size=None),
        ),
    ]
