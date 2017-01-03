from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel


class HomePage(Page):
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

    timeline = RichTextField()
    newsletter = RichTextField()
    members = RichTextField()

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('first_intro'),
                FieldPanel('second_intro'),
            ],
            heading="Header"
        ),
        FieldPanel('description'),
        MultiFieldPanel(
            [
                FieldPanel('topic1'),
                FieldPanel('topic2'),
                FieldPanel('topic3'),
                FieldPanel('topic4'),
            ],
            heading="Topics"
        ),
        FieldPanel('plenary'),
        FieldPanel('discussion'),
        FieldPanel('poster'),
        FieldPanel('timeline'),
        FieldPanel('newsletter'),
        FieldPanel('members'),
    ]
