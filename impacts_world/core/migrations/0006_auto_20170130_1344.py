# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-30 12:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170130_1215'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HeaderLinks',
            new_name='HeaderSettings',
        ),
    ]
