from django import template
from datetime import datetime
register = template.Library()


@register.assignment_tag(takes_context=False)
def timestamp():
    dt = datetime.now()
    ts = dt.microsecond
    return str(ts)
