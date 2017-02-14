from django.utils.text import slugify
from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.blocks import ListBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, RichTextFieldPanel, InlinePanel, FieldPanel, MultiFieldPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailforms.models import AbstractEmailForm
from modelcluster.fields import ParentalKey

from impacts_world.pages.blocks import (
    BASE_BLOCKS, FULL_WIDTH_BLOCKS, COLUMNS_BLOCKS, DayBlock, KeynoteBlock, ContributionBlock, PosterContributionBlock)
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


TIMELINE_ITEM_PLENARY = 'plenary'
TIMELINE_ITEM_WORKSHOP = 'workshop'
TIMELINE_ITEM_POSTER = 'poster'
TIMELINE_ITEM_SPECIAL = 'special'

TIMELINE_ITEM_TYPES = [
    (TIMELINE_ITEM_PLENARY, 'Plenaries'),
    (TIMELINE_ITEM_WORKSHOP, 'Workshops'),
    (TIMELINE_ITEM_POSTER, 'Poster session'),
    (TIMELINE_ITEM_SPECIAL, 'Special event'),
]


class ProgramOverviewPage(Page):
    parent_page_types = ['HomePage', ]
    subpage_types = ['PlenaryOverviewPage', 'WorkshopOverviewPage', 'PosterOverviewPage']
    intro = RichTextField(null=True, blank=True)
    content = StreamField([
        ('day_list', ListBlock(DayBlock, template='blocks/day-list-block.html')),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel('content'),
    ]

    def get_sidebar_menu(self, active_menu_item=None):
        sidebar_menu = [{
            'name': 'Overview',
            'url': self.url,
            'is_active': active_menu_item is None,
        }]
        for child in self.get_children():
            children = []
            for child_child in child.get_children():
                children.append({
                    'name': child_child.title,
                    'url': slugify(child_child.title),
                    'is_active': False,
                })
            sidebar_menu.append({
                'name': child.title,
                'url': child.url,
                'is_active': active_menu_item and isinstance(child.specific, active_menu_item) or False,
                'children': children,
            })
        return sidebar_menu

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['sidebar_menu'] = self.get_sidebar_menu()
        return context


class ProgrammeItemPage(Page):
    description = RichTextField(null=True, blank=True)
    date_time = models.DateTimeField(blank=True, null=True)
    room = models.CharField(max_length=255, blank=True, null=True)
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    parent_page_types = ['ProgramOverviewPage', 'WorkshopChallengePage']

    content_panels = Page.content_panels + [
        FieldPanel('date_time'),
        FieldPanel('room'),
        FieldPanel('description'),
        ImageChooserPanel('icon'),
    ]

    class Meta:
        abstract = True


class PlenaryItemPage(ProgrammeItemPage):
    content = StreamField([
        ('keynote', KeynoteBlock()),
    ], null=True, blank=True)

    content_panels = ProgrammeItemPage.content_panels + [
        StreamFieldPanel('content'),
    ]

    def get_keynotes(self):
        keynotes = []
        for block in self.content:
            keynotes.append({
                'title': block.value.get('title'),
                'name': block.value.get('name'),
                'institute': block.value.get('institute'),
            })
        return keynotes


class WorkshopItemPage(ProgrammeItemPage):
    convenor_name = models.CharField(max_length=500, blank=True, null=True)
    convenor_institute = models.CharField(max_length=500, blank=True, null=True)
    content = StreamField([
        ('contribution', ContributionBlock()),
    ], null=True, blank=True)

    content_panels = ProgrammeItemPage.content_panels + [
        FieldPanel('convenor_name'),
        FieldPanel('convenor_institute'),
        StreamFieldPanel('content'),
    ]


class PosterItemPage(ProgrammeItemPage):
    content = StreamField([
        ('contribution', PosterContributionBlock()),
    ], null=True, blank=True)

    content_panels = ProgrammeItemPage.content_panels + [
        StreamFieldPanel('content'),
    ]


class AbstractOverviewPage(Page):
    intro = RichTextField(null=True, blank=True)
    parent_page_types = ['ProgramOverviewPage', ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    class Meta:
        abstract = True


class PlenaryOverviewPage(AbstractOverviewPage):
    subpage_types = ['PlenaryItemPage', ]
    template = 'pages/plenary_page.html'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['sidebar_menu'] = self.get_parent().specific.get_sidebar_menu(self.content_type.model_class())
        return context


class WorkshopOverviewPage(AbstractOverviewPage):
    subpage_types = ['WorkshopChallengePage', ]
    template = 'pages/workshop_page.html'

    def get_workshops(self, date_time):
        pages = WorkshopItemPage.objects.live().filter(date_time=date_time)
        workshops = []
        for page in pages:
            workshops.append({
                'title': page.title,
                'name': page.convenor_name,
                'institute': page.convenor_institute,
                'url': '%s#%s' % (page.get_parent().get_parent().url, slugify(page.title)),
                'icon': page.icon or page.get_parent().specific.workshop_icon,
                'room': page.room,
            })
        return workshops

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['sidebar_menu'] = self.get_parent().specific.get_sidebar_menu(self.content_type.model_class())
        return context


class WorkshopChallengePage(Page):
    description = RichTextField(null=True, blank=True)
    challenge_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    workshop_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('description'),
        ImageChooserPanel('challenge_icon'),
        ImageChooserPanel('workshop_icon'),
    ]
    parent_page_types = ['WorkshopOverviewPage', ]
    subpage_types = ['WorkshopItemPage', ]


class PosterOverviewPage(AbstractOverviewPage):
    subpage_types = ['PosterItemPage', ]
    template = 'pages/poster_page.html'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['sidebar_menu'] = self.get_parent().specific.get_sidebar_menu(self.content_type.model_class())
        return context
