from datetime import datetime

from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrulestr
from django.utils.timezone import make_aware
from rest_framework import status, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Attendance, Event, Room, Series
from .permissions import KeyholderPermission
from .serialisers import (
    EventEditSerialiser, EventListSerialiser, OwnUserSerialiser,
    RoomSerialiser, SeriesEditSerialiser, SeriesListSerialiser,
)


class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerialiser
    permission_classes = (KeyholderPermission, )


class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    permission_classes = (KeyholderPermission, )

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return SeriesListSerialiser
        return SeriesEditSerialiser

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save(update_fields=['deleted'])


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = (KeyholderPermission, )

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return EventListSerialiser
        return EventEditSerialiser

    def get_queryset(self):
        events = Event.objects.filter(deleted=False)
        if self.action != 'list':
            return events
        events = list(events)
        series_list = Series.objects.all()
        for series in series_list:
            if not series.rrule:
                continue
            year_from_now = datetime.now() + relativedelta(years=1)
            rrule = rrulestr(series.rrule).replace(until=year_from_now)
            for date in rrule:
                start = make_aware(date.replace(
                    hour=series.start.hour, minute=series.start.minute, second=0))
                end = make_aware(date.replace(
                    hour=series.end.hour, minute=series.end.minute, second=0))
                event = Event(name=series.name, description=series.description,
                              start=start, end=end, room=series.room, series=series)
                events.append(event)
        return events

    @detail_route(methods=['post'])
    def attend(self, request, pk):
        event = self.get_object()
        state = request.data.get('state', 'yes')
        if state not in ('yes', 'no', 'maybe'):
            return Response(
                'Status must be yes, no, or maybe, not {state}.'.format(
                    state=state),
                status=status.HTTP_400_BAD_REQUEST,
            )
        if request.user.is_anonymous:
            return Response(
                'User must not be anonymous.',
                status=status.HTTP_400_BAD_REQUEST,
            )
        Attendance.objects.get_or_create(
            event=event, user=request.user, defaults={'state': state})
        return Response(status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save(update_fields=['deleted'])


class FutureEventViewSet(EventViewSet):
    def get_queryset(self):
        if self.action != 'list':
            return EventViewSet.get_queryset(self).filter(end__gte=datetime.now())
        return [x for x in EventViewSet.get_queryset(self) if x.end >= make_aware(datetime.now())]


class OwnUser(APIView):
    def get(self, request):
        serializer = OwnUserSerialiser(request.user)
        return Response(serializer.data)
