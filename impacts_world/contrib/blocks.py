from django import forms
from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property
from django.utils.html import strip_tags
from django.utils.text import slugify
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import StructBlock, FieldBlock, PageChooserBlock, CharBlock, StreamBlock, BooleanBlock, \
    RichTextBlock as _RichTextBlock, URLBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


def smart_truncate(text: str, min_length: int, max_length: int) -> str:
    """
    :param text:
    :param min_length: Minimal length of result string
    :param max_length: Maximal length of result string
    :return: Concattenated String
    """
    if not text:
        return ''
    text = strip_tags(text)
    max_length = len(text) if max_length == 0 else max_length
    c_index = text.rfind('.', min_length, max_length)
    if c_index != -1:
        return text[:c_index + 1]
    else:
        if len(text) > max_length:
            return text[:max_length - 2] + '..'
        else:
            return text


class IntegerBlock(FieldBlock):
    def __init__(self, required=True, help_text=None, max_value=None, min_value=None, **kwargs):
        self.field = forms.IntegerField(required=required, help_text=help_text, max_value=max_value,
                                        min_value=min_value)
        super().__init__(**kwargs)


class EmailBlock(FieldBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        self.field = forms.EmailField(required=required, help_text=help_text)
        super().__init__(**kwargs)


class HeadingBlock(CharBlock):
    class Meta:
        classname = 'full title'
        icon = 'title'
        template = 'widgets/heading.html'

    def get_context(self, value, parent_context=None):
        context = super(HeadingBlock, self).get_context(value, parent_context=parent_context)
        context['text'] = value
        context['slug'] = slugify(value, allow_unicode=True)
        return context


class SubHeadingBlock(CharBlock):
    class Meta:
        icon = 'title'
        template = 'widgets/sub-heading.html'

    def get_context(self, value, parent_context=None):
        context = super(SubHeadingBlock, self).get_context(value, parent_context=parent_context)
        context['text'] = value
        return context


class HRBlock(StreamBlock):
    class Meta:
        icon = 'horizontalrule'
        template = 'widgets/horizontal-ruler.html'


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    is_circled_image = BooleanBlock(required=False, default=False)
    link = URLBlock(required=False)
    open_new_tab = BooleanBlock(required=False, default=True, label="Open link in new tab")

    class Meta:
        icon = 'image'
        template = 'widgets/image.html'

    def get_context(self, value, parent_context=None):
        context = super(ImageBlock, self).get_context(value, parent_context=parent_context)
        if value.get('is_circled_image'):
            context['url'] = value.get('image').get_rendition('fill-1200x1200').url
        else:
            context['url'] = value.get('image').get_rendition('max-1200x1200').url
        context['link'] = value.get('link')
        context['open_new_tab'] = value.get('open_new_tab')
        context['name'] = value.get('image').title
        context['is_circled_image'] = value.get('is_circled_image')
        return context


class ImageContainerBlock(ImageChooserBlock):
    class Meta:
        icon = 'image'
        template = 'widgets/image-container.html'

    def get_context(self, value, parent_context=None):
        context = super(ImageContainerBlock, self).get_context(value, parent_context=parent_context)
        context['url'] = value.get_rendition('max-1200x1200').url
        context['name'] = value.title
        return context


class RichTextBlock(_RichTextBlock):
    class Meta:
        icon = 'pilcrow'
        template = 'widgets/richtext_block.html'

    def get_context(self, value, parent_context=None):
        context = super(RichTextBlock, self).get_context(value, parent_context=parent_context)
        context['content'] = value
        return context


class RichTextContainerBlock(_RichTextBlock):
    class Meta:
        icon = 'pilcrow'
        template = 'widgets/richtext_container_block.html'
        label = 'Rich text'

    def get_context(self, value, parent_context=None):
        context = super(RichTextContainerBlock, self).get_context(value, parent_context=parent_context)
        context['content'] = value
        return context
