from django.contrib import admin

from events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title',  'start_date', 'end_date', 'location',
                    'created', 'is_featured')
    date_hierarcy = 'start_date'
    list_filter = ('start_date',)

admin.site.register(Event, EventAdmin)
