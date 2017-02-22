from __future__ import absolute_import, unicode_literals

import django.forms
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import Widget
from django.forms import (RadioSelect)
from django.utils.html import format_html
from django.utils.encoding import force_str

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailforms.forms import FormBuilder
from wagtail.wagtailforms.models import AbstractFormField, FORM_FIELD_CHOICES

FORM_FIELD_CHOICES = (
    ('heading', _('Heading')),
) + FORM_FIELD_CHOICES


class HeadingWidget(Widget):
    def __init__(self, label, attrs=None):
        self.label = label
        super(HeadingWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        return format_html('<h3>{}</h3>', force_str(self.label))


class HeadingAbstractFormField(AbstractFormField):
    field_type = models.CharField(verbose_name=_('field type'), max_length=16, choices=FORM_FIELD_CHOICES)
    choices = models.TextField(
        verbose_name=_('choices'),
        blank=True,
        help_text=_('Semicolon separated list of choices. Only applicable in checkboxes, radio and dropdown.')
    )
    max_length = models.PositiveIntegerField(
        verbose_name=_('max length'),
        blank=True,
        null=True,
        help_text=_('Max length for single and multiline input fields.')
    )

    panels = [
        FieldPanel('label'),
        FieldPanel('help_text'),
        FieldPanel('required'),
        FieldPanel('field_type', classname="formbuilder-type"),
        FieldPanel('choices', classname="formbuilder-choices"),
        FieldPanel('default_value', classname="formbuilder-default"),
        FieldPanel('max_length', classname="formbuilder-maxlength"),
    ]

    class Meta:
        abstract = True
        ordering = ['sort_order']


class HeadingFormBuilder(FormBuilder):

    def create_heading_field(self, field, options):
        # TODO: This is a default value - it may need to be changed
        options['max_length'] = 255
        options['required'] = False
        return django.forms.CharField(widget=HeadingWidget(label=options.get('label', '')), **options)

    def create_singleline_field(self, field, options):
        if not options['max_length']:
            options['max_length'] = 255
        return django.forms.CharField(**options)

    def create_dropdown_field(self, field, options):
        options['choices'] = map(
            lambda x: (x.strip(), x.strip()),
            field.choices.split(';')
        )
        return django.forms.ChoiceField(**options)

    def create_radio_field(self, field, options):
        options['choices'] = map(
            lambda x: (x.strip(), x.strip()),
            field.choices.split(';')
        )
        return django.forms.ChoiceField(widget=django.forms.RadioSelect, **options)

    def create_checkboxes_field(self, field, options):
        options['choices'] = [(x.strip(), x.strip()) for x in field.choices.split(';')]
        options['initial'] = [x.strip() for x in field.default_value.split(';')]
        return django.forms.MultipleChoiceField(
            widget=django.forms.CheckboxSelectMultiple, **options
        )

    def __init__(self, fields):
        super(HeadingFormBuilder, self).__init__(fields)
        self.FIELD_TYPES.update({
            'heading': HeadingFormBuilder.create_heading_field,
            'singleline': HeadingFormBuilder.create_singleline_field,
            'dropdown': HeadingFormBuilder.create_dropdown_field,
            'radio': HeadingFormBuilder.create_radio_field,
            'checkboxes': HeadingFormBuilder.create_checkboxes_field,
        })

    def get_field_options(self, field):
        options = super(HeadingFormBuilder, self).get_field_options(field)
        if field.field_type in ('singleline', 'multiline'):
            options['max_length'] = field.max_length
        return options
