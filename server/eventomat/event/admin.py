from django.contrib import admin

from .models import Attendance, Event, Room, Series

admin.site.register(Room)
admin.site.register(Event)
admin.site.register(Series)
admin.site.register(Attendance)
