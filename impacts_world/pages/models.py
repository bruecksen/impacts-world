from django.utils.text import slugify
from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, RichTextFieldPanel, InlinePanel, FieldPanel, MultiFieldPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailforms.models import AbstractEmailForm
from modelcluster.fields import ParentalKey

from impacts_world.pages.blocks import BASE_BLOCKS, FULL_WIDTH_BLOCKS, COLUMNS_BLOCKS
from impacts_world.contrib.forms import HeadingFormBuilder, HeadingAbstractFormField
from impacts_world.core.models import TimelineSnippet


class HomePage(Page):
    landing_page_template = 'pages/home_page.html'
    parent_page_types = ['wagtailcore.Page']
    content = StreamField(BASE_BLOCKS + FULL_WIDTH_BLOCKS + COLUMNS_BLOCKS, null=True, blank=True)
    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]


class SidebarPage(Page):
    intro = RichTextField(null=True, blank=True)
    landing_page_template = 'pages/home_page.html'
    parent_page_types = ['wagtailcore.Page', HomePage]
    content = StreamField(BASE_BLOCKS + COLUMNS_BLOCKS, null=True, blank=True)
    content_panels = Page.content_panels + [
        RichTextFieldPanel('intro'),
        StreamFieldPanel('content'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['toc'] = []
        for block in self.content:
            if block.block_type == 'heading':
                link = "#" + slugify(block.value, allow_unicode=True)
                context['toc'] += [{'href': link, 'text': block.value}]
        return context


class GenericPage(Page):
    template = 'pages/default_page.html'
    content = StreamField(BASE_BLOCKS + COLUMNS_BLOCKS, null=True, blank=True)
    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]


class FormField(HeadingAbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')


class FormPage(AbstractEmailForm):
    form_builder = HeadingFormBuilder
    landing_page_template = 'pages/form_page_confirmation.html'
    subpage_types = []
    timeline_snippet = models.ForeignKey(TimelineSnippet, null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    intro = RichTextField(null=True, blank=True)
    confirmation_text = RichTextField(default='The form was submitted successfully. We will get back to you soon.')

    form_title = models.CharField(max_length=500, verbose_name='Form title', null=True, blank=True)
    button_name = models.CharField(max_length=500, verbose_name='Button name', default='Submit')

    content_panels = AbstractEmailForm.content_panels + [
        SnippetChooserPanel('timeline_snippet'),
        FieldPanel('intro'),
        MultiFieldPanel([
            FieldPanel('form_title'),
            InlinePanel('form_fields', label="Form fields"),
            FieldPanel('button_name'),
            FieldPanel('confirmation_text', classname="full"),
            MultiFieldPanel([
                FieldPanel('to_address', classname="full"),
                FieldPanel('from_address', classname="full"),
                FieldPanel('subject', classname="full"),
            ], "Email"),
        ], "Form Builder"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context
