from django.utils.text import slugify

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, RichTextFieldPanel

from .blocks import BASE_BLOCKS, FULL_WIDTH_BLOCKS, COLUMNS_BLOCKS


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
