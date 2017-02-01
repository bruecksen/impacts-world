from wagtail.wagtailcore import blocks
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from impacts_world.core.models import TimelineSnippet
from impacts_world.contrib.blocks import RichTextBlock
from wagtail.wagtailembeds.blocks import EmbedBlock


class TimelineBlock(blocks.StructBlock):
    snippet = SnippetChooserBlock(TimelineSnippet)

    class Meta:
        icon = 'date'
        template = 'blocks/timeline_block.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['timeline'] = value.get('snippet')
        return context


class TeaserBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(required=True)
    page = blocks.PageChooserBlock(required=True)

    class Meta:
        icon = 'pick'
        template = 'blocks/teaser_block.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['text'] = value.get('text')
        context['page_url'] = value.get('page').url
        return context


class VideoTeaserBlock(blocks.StructBlock):
    video = EmbedBlock(required=True)
    text = blocks.RichTextBlock(required=True)

    class Meta:
        icon = 'media'
        template = 'blocks/video_teaser_block.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['text'] = value.get('text')
        context['video'] = value.get('video')
        return context


class ChallengeBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True)
    short_description = RichTextBlock(required=True)


class ChallengesBlock(blocks.StructBlock):
    intro = blocks.RichTextBlock(required=True)
    challenge1 = ChallengeBlock(required=True)
    challenge2 = ChallengeBlock(required=True)
    challenge3 = ChallengeBlock(required=True)
    challenge4 = ChallengeBlock(required=True)

    class Meta:
        icon = 'grip'
        template = 'blocks/challenges_block.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['intro'] = value.get('intro')
        context['challenge1'] = value.get('challenge1')
        context['challenge2'] = value.get('challenge2')
        context['challenge3'] = value.get('challenge3')
        context['challenge4'] = value.get('challenge4')
        return context


class Testimonial(blocks.StructBlock):
    name = blocks.CharBlock(required=True)
    institute = blocks.CharBlock(required=False)
    testimonial = blocks.TextBlock(required=True)
    picture = ImageChooserBlock(required=True)


class Testimonials(blocks.StructBlock):
    testimonials = blocks.ListBlock(Testimonial)

    class Meta:
        icon = 'openquote'
        template = 'blocks/testimonials_block.html'

    def get_context(self, value):
        context = super().get_context(value)
        testimonials = value.get('testimonials')
        # split testimonials in chunks of 3 to make it work with the slider
        chunks = [testimonials[i:i + 3] for i in range(0, len(testimonials), 3)]
        context['testimonials'] = chunks
        return context


BASE_BLOCKS = [
    ('timeline', TimelineBlock()),
    ('rich_text', RichTextBlock()),
    ('teaser', TeaserBlock()),
    ('video_teaser', VideoTeaserBlock()),
    ('challenge', ChallengesBlock()),
    ('testimonials', Testimonials())

    # ('horizontal_ruler', HRBlock()),
    # ('embed', EmbedBlock()),
    # ('image', ImageBlock()),
]

COLUMNS_BLOCKS = [
    # ('columns_1_to_1', Columns1To1Block()),
    # ('columns_1_to_2', Columns1To2Block()),
    # ('columns_2_to_1', Columns2To1Block()),
    # ('columns_1_to_1_to_1', Columns1To1To1Block()),
    # ('columns_1_to_1_to_1_to_1', Columns1To1To1To1Block()),
]
