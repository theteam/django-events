from django.db import models
from django.utils.translation import ugettext as _

from djqmgr import QManager
from django_extensions.db.fields import CreationDateTimeField,\
     ModificationDateTimeField, AutoSlugField

class Event(models.Model):
    """Events"""
    LIVE = 1
    HIDDEN = 2
    REMOVED = 3
    STATUS_CHOICES = ((LIVE, _('Live')),
                      (HIDDEN, _('Hidden')),
                      (REMOVED, _('Removed')),
                      )
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    summary = models.TextField(blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="event", blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(blank=True, max_length=255)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()
    status = models.IntegerField(choices=STATUS_CHOICES,
                                 default=LIVE)
    is_featured = models.BooleanField(default=False)
    url = models.URLField(verify_exists=False, blank=True)

    # managers
    objects = models.Manager()
    live = QManager(status=LIVE)

    def __unicode__(self):
        return u'Event: %s ' % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('events:event_detail', [self.slug,])
