from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.wagtailcore.fields import RichTextField
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailcore.models import Orderable


@register_setting(icon='list-ul')
class HeaderSettings(ClusterableModel, BaseSetting):
    banner_first_intro = RichTextField(null=True, blank=True)
    banner_second_intro = RichTextField(null=True, blank=True)
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    show_participate = models.BooleanField(default=False)
    participate_target = models.ForeignKey('wagtailcore.Page', null=True, blank=True)
    participate_alt_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Alt. name', help_text='If left empty, the target\'s title will be used.')
    participate_name = property(lambda self: self.participate_alt_name or self.participate_target.title)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('banner_first_intro'),
                FieldPanel('banner_second_intro'),
                ImageChooserPanel('banner_image'),
            ],
            heading="Banner",
        ),
        InlinePanel('header_links', label="Link", classname="collapsed"),
        MultiFieldPanel(
            [
                FieldPanel('show_participate'),
                FieldPanel('participate_alt_name'),
                PageChooserPanel('participate_target'),
            ],
            heading="Participate",
        ),
    ]


class HeaderLink(Orderable, models.Model):
    header = ParentalKey(HeaderSettings, related_name='header_links')
    target = models.ForeignKey('wagtailcore.Page')
    _name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Alt. name',
                             help_text='If left empty, the target\'s title will be used.')
    name = property(lambda self: self._name or self.target.title)

    panels = [
        PageChooserPanel('target'),
        FieldPanel('_name'),
    ]


@register_snippet
class TimelineSnippet(ClusterableModel):
    title = models.CharField(max_length=500)
    panels = [
        FieldPanel('title'),
        InlinePanel('timeline_items', label='Timeline item'),
    ]

    def __str__(self):
        return self.title


class TimelineItem(Orderable, models.Model):
    timeline = ParentalKey(TimelineSnippet, related_name='timeline_items')
    title = models.CharField(max_length=500)
    date = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=False, help_text='Currently active item.')

    panels = [
        FieldPanel('title'),
        FieldPanel('date'),
        FieldPanel('is_active'),
    ]
