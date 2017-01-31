# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-30 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170130_1435'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Timeline',
            new_name='TimelineSnippet',
        ),
        migrations.AlterField(
            model_name='timelineitem',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Currently active item.'),
        ),
    ]
