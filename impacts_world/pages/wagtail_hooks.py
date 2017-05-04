from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_css')
def editor_css():
    # add some extra width to highly nested elements in the wagtail editor
    return """
        <style>
            li.sequence-member .struct-block .sequence-container {
                width: 83.3333333%;
            }
            li.sequence-member .sequence-member-inner .sequence-type-list .sequence-container-inner {
                width: 100%;
            }
            li.sequence-member .struct-block .fields {
                width: calc(100% - 100px);  // 100 pixels for the reorder/delete buttons.
            }
        </style>
    """
