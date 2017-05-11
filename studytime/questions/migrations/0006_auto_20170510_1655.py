# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 16:55
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20170510_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiplechoiceanswer',
            name='answer_array',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], max_length=1), blank=True, default=[], null=True, size=None),
        ),
    ]
