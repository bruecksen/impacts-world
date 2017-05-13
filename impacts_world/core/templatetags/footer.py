from django import template
from django.template.loader import render_to_string

from impacts_world.pages.models import FooterSettings
register = template.Library()


@register.simple_tag(takes_context=True)
def footer(context, *args, **kwargs):
    request = context['request']
    settings = FooterSettings.for_site(request.site)

    context['footer'] = settings.content
    context.update(kwargs)
    template = 'widgets/footer.html'
    return render_to_string(template, context=context.flatten())
