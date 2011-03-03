from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from events.models import Event

def object_list(request, template='events/object_list.html'):
    """List of the ``LIVE`` ``Event`` ordered by Featured and Date"""
    object_list = Event.live.all().order_by('is_featured','-created')
    extra_context = {'object_list': object_list,}
    return render_to_response(template, extra_context,
                              RequestContext(request))

def object_detail(request, slug, template='events/object_detail.html'):
    """Shows the requested ``EVENT`` if ``LIVE``"""
    event = get_object_or_404(Event, slug=slug, status=Event.LIVE)
    extra_context = {'object': event}
    return render_to_response(template, extra_context,
                              RequestContext(request))
