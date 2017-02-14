import uuid
from django.conf import settings
from django.utils.text import slugify

from wagtail.wagtailcore.blocks import StreamBlock, PageChooserBlock, StructBlock, CharBlock, \
    TextBlock, ListBlock, TimeBlock, DateBlock, BooleanBlock
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

# from impacts_world.pages.models import PlenaryItemPage
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
    icon = ImageChooserBlock(required=True)
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


class AbstractPanelBlock(StructBlock):

    class Meta:
        abstract = True

    def get_context(self, value):
        context = super().get_context(value)
        description = value.get('description')
        context['is_collapsible'] = False
        if description:
            context['is_collapsible'] = True
        context['description'] = description
        context['title'] = value.get('title', '')
        context['time'] = value.get('time', None)
        context['panel_id'] = uuid.uuid4()
        return context


class PlenaryBlock(AbstractPanelBlock):
    title = CharBlock(required=True, classname='title-field')
    description = RichTextBlock(required=False)
    plenary_page = PageChooserBlock(required=True, target_model='pages.PlenaryItemPage')

    class Meta:
        label = 'Planery'
        template = 'blocks/programme-plenary-block.html'
        icon = 'user'

    def get_context(self, value):
        context = super().get_context(value)
        plenary_page = value.get('plenary_page')
        context['time'] = plenary_page.date_time
        keynotes = plenary_page.get_keynotes()
        context['keynotes'] = keynotes
        context['plenary_url'] = "%s#%s" % (plenary_page.get_parent().url, slugify(plenary_page.title))
        if keynotes:
            context['is_collapsible'] = True
        return context


class WorkshopBlock(AbstractPanelBlock):
    title = CharBlock(required=True, classname='title-field')
    description = RichTextBlock(required=False)
    workshop_page = PageChooserBlock(required=True, target_model='pages.WorkshopItemPage')

    class Meta:
        label = 'Workshop'
        template = 'blocks/programme-workshop-block.html'
        icon = 'group'

    def get_context(self, value):
        context = super().get_context(value)
        workshop_page = value.get('workshop_page')
        date_time = workshop_page.date_time
        context['time'] = date_time
        workshops = workshop_page.get_parent().get_parent().specific.get_workshops(date_time)
        context['workshops'] = workshops
        if workshops:
            context['is_collapsible'] = True
        return context


class PosterBlock(AbstractPanelBlock):
    title = CharBlock(required=True, classname='title-field')
    description = RichTextBlock(required=False)
    poster_page = PageChooserBlock(required=True, target_model='pages.PosterItemPage')

    class Meta:
        label = 'Poster'
        template = 'blocks/programme-poster-block.html'
        icon = 'doc-full-inverse'

    def get_context(self, value):
        context = super().get_context(value)
        context['time'] = value.get('poster_page').date_time
        return context


class SpecialEventBlock(AbstractPanelBlock):
    time = TimeBlock(required=True, classname='time-field')
    title = CharBlock(required=True, classname='title-field')
    description = RichTextBlock(required=False)

    class Meta:
        label = 'Special event'
        template = 'blocks/programme-plenary-block.html'
        icon = 'pick'


class RefreshmentBlock(AbstractPanelBlock):
    time = TimeBlock(required=True, classname='time-field')
    title = CharBlock(required=True, classname='title-field')
    description = RichTextBlock(required=False)

    class Meta:
        label = 'Refreshment'
        template = 'blocks/programme-plenary-block.html'
        icon = 'time'


PANEL_BLOCKS = [
    ('refreshment', RefreshmentBlock()),
    ('plenary', PlenaryBlock()),
    ('workshop', WorkshopBlock()),
    ('poster', PosterBlock()),
    ('special_event', SpecialEventBlock()),
]


class DayBlock(StructBlock):
    date = DateBlock(required=True, classname='date-field')
    title = CharBlock(required=True, classname='title-field')
    panels = StreamBlock(PANEL_BLOCKS)

    class Meta:
        label = 'Day'
        template = 'blocks/programme-day-block.html'
        icon = 'date'

    def get_context(self, value):
        context = super().get_context(value)
        context['title'] = value.get('title')
        context['date'] = value.get('date')
        context['panels'] = value.get('panels')
        return context


class KeynoteBlock(StructBlock):
    title = CharBlock(required=True)
    description = RichTextBlock(required=True)
    name = CharBlock(required=True)
    institute = CharBlock(required=True)
    picture = ImageChooserBlock(required=True)

    class Meta:
        label = 'Keynote'
        template = 'blocks/keynote-block.html'
        icon = 'password'

    def get_context(self, value):
        context = super().get_context(value)
        context['title'] = value.get('title')
        context['description'] = value.get('description')
        context['name'] = value.get('name')
        context['institute'] = value.get('institute')
        context['picture'] = value.get('picture')
        return context


class ContributionBlock(StructBlock):
    title = CharBlock(required=True)
    name = CharBlock(required=True)
    institute = CharBlock(required=True)
    description = RichTextBlock(required=True)

    class Meta:
        label = 'Contribution'
        template = 'blocks/contribution-block.html'
        icon = 'password'

    def get_context(self, value):
        context = super().get_context(value)
        context['title'] = value.get('title')
        context['subtitle'] = "(%s, %s)" % (value.get('name'), value.get('institute'))
        context['description'] = value.get('description')
        context['panel_id'] = uuid.uuid4()
        return context


class PosterContributionBlock(StructBlock):
    number = CharBlock(required=True)
    title = CharBlock(required=True)
    authors = RichTextBlock(required=True)
    description = RichTextBlock(required=True)

    class Meta:
        label = 'Contribution'
        template = 'blocks/poster-contribution-block.html'
        icon = 'password'

    def get_context(self, value):
        context = super().get_context(value)
        context['number'] = value.get('number')
        context['title'] = value.get('title')
        context['authors'] = value.get('authors')
        context['description'] = value.get('description')
        context['panel_id'] = uuid.uuid4()
        return context
