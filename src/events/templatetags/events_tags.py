from django import template
from django.template import RequestContext
from django.template.loader import render_to_string

from templatetag_sugar.register import tag
from templatetag_sugar.parser import Constant, Optional, Variable
from events.models import Event

register = template.Library()

@tag(register, [Optional([Constant("with"), Variable()])])
def render_latest_events(context, template='events/shortlist.html'):
    """Renders the site sponsors
    Takes: "with TEMPLATE_NAME" as an optional parameter
    {% render_latest_events with "events/shortlist.html" %}
    """
    request = context.get('request')
    object_list = Event.live.all().order_by('-start_date')[:5]
    extra_context = {'object_list': object_list}
    template_context = RequestContext(request, extra_context)
    return render_to_string(template, template_context)
