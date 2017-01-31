from wagtail.wagtailcore import blocks
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock

from impacts_world.core.models import TimelineSnippet
from impacts_world.contrib.blocks import RichTextBlock


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
    text = blocks.RichTextBlock()
    page = blocks.PageChooserBlock()

    class Meta:
        icon = 'pick'
        template = 'blocks/teaser_block.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['text'] = value.get('text')
        context['page_url'] = value.get('page').url
        return context


class ChallengeBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True)
    short_description = RichTextBlock(required=True)


class ChallengesBlock(blocks.StructBlock):
    intro = blocks.RichTextBlock()
    challenge1 = ChallengeBlock()
    challenge2 = ChallengeBlock()
    challenge3 = ChallengeBlock()
    challenge4 = ChallengeBlock()

    class Meta:
        icon = 'grip'
        template = 'blocks/challenges_block.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['text'] = value.get('text')
        context['page_url'] = value.get('page').url
        return context


BASE_BLOCKS = [
    ('timeline', TimelineBlock()),
    ('rich_text', RichTextBlock()),
    ('teaser', TeaserBlock()),
    ('challenge', ChallengesBlock()),
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
