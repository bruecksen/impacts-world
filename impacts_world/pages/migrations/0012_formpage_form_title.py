# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-06 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20170206_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpage',
            name='form_title',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Form title'),
        ),
    ]