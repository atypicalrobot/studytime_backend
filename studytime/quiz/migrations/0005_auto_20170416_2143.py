# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20170416_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiplechoicequestion',
            name='reprompt_text',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='question',
            name='reprompt_text',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='trueorfalsequestion',
            name='reprompt_text',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
