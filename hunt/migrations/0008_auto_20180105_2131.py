# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-05 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0007_submission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='level',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='user',
        ),
        migrations.DeleteModel(
            name='Submission',
        ),
    ]
