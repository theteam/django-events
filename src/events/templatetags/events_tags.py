from django import template

from events.models import Event

register = template.Library()

@register.inclusion_tag('events/shortlist.html', takes_context=True)
def render_latest_events(context):
    """Renders the site sponsors"""
    object_list = Event.live.all().order_by('-start_date')[:5]
    return {'object_list': object_list}
