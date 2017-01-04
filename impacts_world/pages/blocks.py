from wagtail.wagtailcore import blocks


class TimelineBlock(blocks.StructBlock):
    date = blocks.DateBlock(required=True)
    text = blocks.RichTextBlock()

    class Meta:
        icon = 'date'
        template = 'blocks/timeline_block.html'
