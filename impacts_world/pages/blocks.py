import uuid
from django.conf import settings
from django.utils.text import slugify

from wagtail.wagtailcore.blocks import StreamBlock, PageChooserBlock, StructBlock, CharBlock, \
    TextBlock, ListBlock, TimeBlock, DateBlock, BooleanBlock
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from impacts_world.core.models import TimelineSnippet
from impacts_world.contrib.blocks import RichTextBlock, RichTextContainerBlock, ImageBlock, \
    ImageContainerBlock, HeadingBlock, SubHeadingBlock
from wagtail.wagtailembeds.blocks import EmbedBlock


class TimelineBlock(StructBlock):
    snippet = SnippetChooserBlock(TimelineSnippet)

    class Meta:
        icon = 'date'
        template = 'blocks/timeline_block.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['timeline'] = value.get('snippet')
        return context


class TeaserBlock(StructBlock):
    text = RichTextBlock(required=True)
    page = PageChooserBlock(required=True)

    class Meta:
        icon = 'pick'
        template = 'blocks/teaser_block.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['text'] = value.get('text')
        if value.get('page'):
            context['page_url'] = value.get('page').url
        return context


class VideoTeaserBlock(StructBlock):
    video = EmbedBlock(required=True)
    text = RichTextBlock(required=True)

    class Meta:
        icon = 'media'
        template = 'blocks/video_teaser_block.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['text'] = value.get('text')
        context['video'] = value.get('video')
        return context


class ChallengeBlock(StructBlock):
    name = CharBlock(required=True)
    short_description = RichTextBlock(required=True)


class ChallengesBlock(StructBlock):
    intro = RichTextBlock(required=True)
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


class Testimonial(StructBlock):
    name = CharBlock(required=True)
    institute = CharBlock(required=False)
    testimonial = TextBlock(required=True)
    picture = ImageChooserBlock(required=True)


class Testimonials(StructBlock):
    testimonials = ListBlock(Testimonial)

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


class GoogleMapBlock(StructBlock):
    map_lat = CharBlock(required=True, max_length=255, label='Latitude', default='52.520645')
    map_long = CharBlock(required=True, max_length=255, label='Longitude', default='13.409779')
    map_zoom_level = CharBlock(default=14, required=True, max_length=3, label='Map zoom level')

    class Meta:
        template = 'blocks/google_map_block.html'
        icon = 'tag'
        label = 'Google Map'

    def get_context(self, value):
        context = super().get_context(value)
        context['GOOGLE_MAPS_V3_APIKEY'] = settings.GOOGLE_MAPS_V3_APIKEY
        return context


BASE_BLOCKS = [
    ('heading', HeadingBlock()),
    ('sub_heading', SubHeadingBlock()),
    ('rich_text_container', RichTextContainerBlock()),
    ('image_container', ImageContainerBlock()),
    ('teaser', TeaserBlock()),
    ('video_teaser', VideoTeaserBlock()),
    ('testimonials', Testimonials()),
    ('google_map', GoogleMapBlock()),
]

FULL_WIDTH_BLOCKS = [
    ('challenge', ChallengesBlock()),
    ('timeline', TimelineBlock()),
]

_COLUMNS_BLOCKS = [
    ('rich_text', RichTextBlock()),
    ('image', ImageBlock()),
    ('google_map', GoogleMapBlock()),
]


class ColumnsBlock(StructBlock):
    left_column = StreamBlock(_COLUMNS_BLOCKS)
    right_column = StreamBlock(_COLUMNS_BLOCKS)  # , form_classname='pull-right')

    def get_context(self, value):
        context = super().get_context(value)
        context['left_column'] = value.get('left_column')
        context['right_column'] = value.get('right_column')
        return context

    class Meta:
        icon = 'table'
        label = 'Columns 1-1'
        template = None


class Columns1To1Block(ColumnsBlock):
    class Meta:
        label = 'Columns 1:1'
        template = 'blocks/columns-1-1.html'


class Columns1To2Block(ColumnsBlock):
    class Meta:
        label = 'Columns 1:2'
        template = 'blocks/columns-1-2.html'


class Columns1To3Block(ColumnsBlock):
    class Meta:
        label = 'Columns 1:3'
        template = 'blocks/columns-1-3.html'


class Columns2To1Block(ColumnsBlock):
    class Meta:
        label = 'Columns 2:1'
        template = 'blocks/columns-2-1.html'


class Columns1To1To1Block(StructBlock):
    left_column = StreamBlock(_COLUMNS_BLOCKS)
    center_column = StreamBlock(_COLUMNS_BLOCKS)
    right_column = StreamBlock(_COLUMNS_BLOCKS)

    class Meta:
        label = 'Columns 1:1:1'
        template = 'blocks/columns-1-1-1.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['left_column'] = value.get('left_column')
        context['center_column'] = value.get('center_column')
        context['right_column'] = value.get('right_column')
        return context


class Columns1To1To1To1Block(StructBlock):
    first_column = StreamBlock(_COLUMNS_BLOCKS)
    second_column = StreamBlock(_COLUMNS_BLOCKS)
    third_column = StreamBlock(_COLUMNS_BLOCKS)
    fourth_column = StreamBlock(_COLUMNS_BLOCKS)

    class Meta:
        label = 'Columns 1:1:1:1'
        template = 'blocks/columns-1-1-1-1.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['first_column'] = value.get('first_column')
        context['second_column'] = value.get('second_column')
        context['third_column'] = value.get('third_column')
        context['fourth_column'] = value.get('fourth_column')
        return context


COLUMNS_BLOCKS = [
    ('columns_1_to_1', Columns1To1Block()),
    ('columns_1_to_2', Columns1To2Block()),
    ('columns_1_to_3', Columns1To3Block()),
    ('columns_2_to_1', Columns2To1Block()),
    ('columns_1_to_1_to_1', Columns1To1To1Block()),
    ('columns_1_to_1_to_1_to_1', Columns1To1To1To1Block()),
]


class DayBlock(StructBlock):
    title = CharBlock(required=True)
    date = DateBlock(required=True)

    class Meta:
        label = 'Day'
        template = 'blocks/programme-day-block.html'
        icon = 'title'


class PanelBlock(StructBlock):
    time = TimeBlock(required=True)
    title = CharBlock(required=True)
    description = RichTextBlock(required=False)
    is_collapsible = BooleanBlock(default=True, required=False)

    class Meta:
        abstract = True

    def get_context(self, value):
        context = super().get_context(value)
        context['description'] = value.get('description', '')
        context['title'] = value.get('title', '')
        context['time'] = value.get('time', None)
        context['panel_id'] = self.get_unique_identifier()
        context['is_collapsible'] = value.get('is_collapsible', None)
        return context

    def get_unique_identifier(self):
        return uuid.uuid4()


class PlenaryBlock(PanelBlock):
    class Meta:
        label = 'Planery'
        template = 'blocks/programme-plenary-block.html'
        icon = 'user'


class WorkshopBlock(PanelBlock):
    class Meta:
        label = 'Workshop'
        template = 'blocks/programme-plenary-block.html'
        icon = 'group'


class PosterBlock(PanelBlock):
    class Meta:
        label = 'Poster'
        template = 'blocks/programme-plenary-block.html'
        icon = 'doc-full-inverse'


class SpecialEventBlock(PanelBlock):
    class Meta:
        label = 'Special event'
        template = 'blocks/programme-plenary-block.html'
        icon = 'pick'


class RefreshmentBlock(PanelBlock):
    class Meta:
        label = 'Refreshment'
        template = 'blocks/programme-plenary-block.html'
        icon = 'time'


PANEL_BLOCKS = [
    ('day', DayBlock()),
    ('refreshment', RefreshmentBlock()),
    ('plenary', PlenaryBlock()),
    ('workshop', WorkshopBlock()),
    ('poster', PosterBlock()),
    ('special_event', SpecialEventBlock()),
]
