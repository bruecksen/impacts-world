from django import template
from django.template.loader import render_to_string

from impacts_world.core.models import HeaderSettings
register = template.Library()


@register.simple_tag(takes_context=True)
def header(context, *args, **kwargs):
    request = context['request']
    settings = HeaderSettings.for_site(request.site)

    page = context.get('page')

    links = []
    for link in settings.header_links.all():
        name = link.name
        target = link.target.specific
        if page and target == page:
            active = True
        else:
            active = False
        if target.url:
            links.append({'url': target.url, 'text': name, 'active': active})

    if settings.show_participate:
        name = settings.participate_name
        target = settings.participate_target.specific
        if page and target == page:
            active = True
        else:
            active = False
        if target.url:
            context['participate'] = {'url': target.url, 'text': name, 'active': active}

    if kwargs.get('show_banner', False):
        rendition = settings.banner_image.get_rendition('fill-1200x520-c100')
        context['banner'] = {
            'first_intro': settings.banner_first_intro,
            'second_intro': settings.banner_second_intro,
            'image': rendition.url,
        }
    context['links'] = links
    context.update(kwargs)
    template = 'widgets/header.html'
    return render_to_string(template, context=context.flatten())
