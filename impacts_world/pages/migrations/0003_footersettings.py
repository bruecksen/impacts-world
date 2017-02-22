# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-21 10:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import impacts_world.contrib.blocks
import impacts_world.pages.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('pages', '0002_formpage_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', wagtail.wagtailcore.fields.StreamField((('heading', impacts_world.contrib.blocks.HeadingBlock()), ('sub_heading', impacts_world.contrib.blocks.SubHeadingBlock()), ('rich_text_container', impacts_world.contrib.blocks.RichTextContainerBlock()), ('image_container', impacts_world.contrib.blocks.ImageContainerBlock()), ('teaser', wagtail.wagtailcore.blocks.StructBlock((('text', impacts_world.contrib.blocks.RichTextBlock(required=True)), ('page', wagtail.wagtailcore.blocks.PageChooserBlock(required=True))))), ('video_teaser', wagtail.wagtailcore.blocks.StructBlock((('video', wagtail.wagtailembeds.blocks.EmbedBlock(required=True)), ('text', impacts_world.contrib.blocks.RichTextBlock(required=True))))), ('testimonials', wagtail.wagtailcore.blocks.StructBlock((('testimonials', wagtail.wagtailcore.blocks.ListBlock(impacts_world.pages.blocks.Testimonial)),))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True))))), ('columns_1_to_1', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', impacts_world.contrib.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('is_circled_image', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True)))))))), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', impacts_world.contrib.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('is_circled_image', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True))))))))))), ('columns_1_to_2', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', impacts_world.contrib.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('is_circled_image', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True)))))))), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', impacts_world.contrib.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('is_circled_image', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True))))))))))), ('columns_1_to_3', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', impacts_world.contrib.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('is_circled_image', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True)))))))), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', impacts_world.contrib.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('is_circled_image', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True))))))))))), ('columns_2_to_1', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', impacts_world.contrib.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('is_circled_image', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True)))))))), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', impacts_world.contrib.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('is_circled_image', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True))))))))))), ('columns_1_to_1_to_1', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', impacts_world.contrib.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('is_circled_image', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True)))))))), ('center_column', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', impacts_world.contrib.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('is_circled_image', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True)))))))), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', impacts_world.contrib.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('is_circled_image', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True))))))))))), ('columns_1_to_1_to_1_to_1', wagtail.wagtailcore.blocks.StructBlock((('first_column', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', impacts_world.contrib.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('is_circled_image', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True)))))))), ('second_column', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', impacts_world.contrib.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('is_circled_image', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True)))))))), ('third_column', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', impacts_world.contrib.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('is_circled_image', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True)))))))), ('fourth_column', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', impacts_world.contrib.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('is_circled_image', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_lat', wagtail.wagtailcore.blocks.CharBlock(default='52.520645', label='Latitude', max_length=255, required=True)), ('map_long', wagtail.wagtailcore.blocks.CharBlock(default='13.409779', label='Longitude', max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, label='Map zoom level', max_length=3, required=True)))))))))))), blank=True, null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]