from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import InlinePanel, FieldPanel, MultiFieldPanel, StreamFieldPanel, FieldRowPanel
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField

from .blocks import TimelineBlock

class FormField(AbstractFormField):
    page = ParentalKey('HomePage', related_name='form_fields')


class HomePage(AbstractEmailForm):
    landing_page_template = 'pages/home_page.html'
    parent_page_types = ['wagtailcore.Page']

    first_intro = RichTextField()
    second_intro = RichTextField()

    description = RichTextField()

    topic1 = RichTextField()
    topic2 = RichTextField()
    topic3 = RichTextField()
    topic4 = RichTextField()

    plenary = RichTextField()
    discussion = RichTextField()
    poster = RichTextField()

    timeline = StreamField([('event', TimelineBlock()), ])
    newsletter = RichTextField()
    members1 = RichTextField()
    members2 = RichTextField()
    members3 = RichTextField()

    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('first_intro'),
                FieldPanel('second_intro'),
            ],
            heading='Header'
        ),
        FieldPanel('description'),
        MultiFieldPanel(
            [
                FieldPanel('topic1'),
                FieldPanel('topic2'),
                FieldPanel('topic3'),
                FieldPanel('topic4'),
            ],
            heading='Topics'
        ),
        FieldPanel('plenary'),
        FieldPanel('discussion'),
        FieldPanel('poster'),
        StreamFieldPanel('timeline'),
        FieldPanel('newsletter'),
        MultiFieldPanel(
            [
                FieldPanel('members1'),
                FieldPanel('members2'),
                FieldPanel('members3'),
            ],
            heading='Members'
        ),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]
