from django import forms
from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property
from django.utils.html import strip_tags
from django.utils.text import slugify
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import FieldBlock, PageChooserBlock, CharBlock, StreamBlock, BooleanBlock, \
    RichTextBlock as _RichTextBlock
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

    def get_context(self, value):
        context = super().get_context(value)
        context['text'] = value
        context['slug'] = slugify(value, allow_unicode=True)
        return context


class HRBlock(StreamBlock):
    class Meta:
        icon = 'horizontalrule'
        template = 'widgets/horizontal-ruler.html'


class ImageBlock(ImageChooserBlock):
    class Meta:
        icon = 'image'
        template = 'widgets/image.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['url'] = value.get_rendition('max-1200x1200').url
        context['name'] = value.title
        return context


class ImageContainerBlock(ImageChooserBlock):
    class Meta:
        icon = 'image'
        template = 'widgets/image-container.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['url'] = value.get_rendition('max-1200x1200').url
        context['name'] = value.title
        return context


class RichTextBlock(_RichTextBlock):
    class Meta:
        icon = 'pilcrow'
        template = 'widgets/richtext_block.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['content'] = value
        return context


class RichTextContainerBlock(_RichTextBlock):
    class Meta:
        icon = 'pilcrow'
        template = 'widgets/richtext_container_block.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['content'] = value
        return context
