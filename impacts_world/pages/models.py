from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import InlinePanel, FieldPanel, MultiFieldPanel, StreamFieldPanel, FieldRowPanel
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField

from .blocks import BASE_BLOCKS, COLUMNS_BLOCKS


class HomePage(Page):
    landing_page_template = 'pages/home_page.html'
    parent_page_types = ['wagtailcore.Page']
    content = StreamField(BASE_BLOCKS + COLUMNS_BLOCKS, null=True, blank=True)
    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]


class GenericPage(Page):
    template = 'pages/default_page.html'
    content = StreamField(BASE_BLOCKS + COLUMNS_BLOCKS, null=True, blank=True)
    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]
