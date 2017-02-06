from __future__ import absolute_import, unicode_literals

import django.forms
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import Widget
from django.forms import (CheckboxSelectMultiple, RadioSelect)
from django.utils.html import format_html
from django.utils.encoding import force_str

from wagtail.wagtailforms.forms import FormBuilder
from wagtail.wagtailforms.models import AbstractFormField, FORM_FIELD_CHOICES

from bootstrap3.renderers import FieldRenderer
from bootstrap3.text import text_value
from bootstrap3.utils import add_css_class

FORM_FIELD_CHOICES = (
    ('heading', _('Heading')),
) + FORM_FIELD_CHOICES


class LabelFieldRenderer(FieldRenderer):
    WIDGETS_SHOW_LABEL = (
        CheckboxSelectMultiple,
        RadioSelect,
    )

    def get_label_class(self):
        label_class = self.label_class
        widget = self.widget
        if not label_class and self.layout == 'horizontal':
            label_class = self.horizontal_label_class
        label_class = text_value(label_class)
        if not isinstance(widget, self.WIDGETS_SHOW_LABEL) and not self.show_label:
            label_class = add_css_class(label_class, 'sr-only')
        return add_css_class(label_class, 'control-label')


class HeadingWidget(Widget):
    def __init__(self, label, attrs=None):
        self.label = label
        super(HeadingWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        return format_html('<h3>{}</h3>', force_str(self.label))


class HeadingAbstractFormField(AbstractFormField):
    field_type = models.CharField(verbose_name=_('field type'), max_length=16, choices=FORM_FIELD_CHOICES)

    class Meta:
        abstract = True
        ordering = ['sort_order']


class HeadingFormBuilder(FormBuilder):

    def create_heading_field(self, field, options):
        # TODO: This is a default value - it may need to be changed
        options['max_length'] = 255
        options['required'] = False
        return django.forms.CharField(widget=HeadingWidget(label=options.get('label', '')), **options)

    def __init__(self, fields):
        super(HeadingFormBuilder, self).__init__(fields)
        self.FIELD_TYPES.update({
            'heading': HeadingFormBuilder.create_heading_field
        })
