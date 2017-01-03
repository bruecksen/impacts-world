# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('first_intro', wagtail.wagtailcore.fields.RichTextField()),
                ('second_intro', wagtail.wagtailcore.fields.RichTextField()),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
                ('topic1', wagtail.wagtailcore.fields.RichTextField()),
                ('topic2', wagtail.wagtailcore.fields.RichTextField()),
                ('topic3', wagtail.wagtailcore.fields.RichTextField()),
                ('topic4', wagtail.wagtailcore.fields.RichTextField()),
                ('plenary', wagtail.wagtailcore.fields.RichTextField()),
                ('discussion', wagtail.wagtailcore.fields.RichTextField()),
                ('poster', wagtail.wagtailcore.fields.RichTextField()),
                ('timeline', wagtail.wagtailcore.fields.RichTextField()),
                ('newsletter', wagtail.wagtailcore.fields.RichTextField()),
                ('members', wagtail.wagtailcore.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
