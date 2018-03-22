from rest_framework import viewsets

from .models import Event, Room, Series
from .permissions import KeyholderPermission
from .serialisers import EventSerialiser, RoomSerialiser, SeriesSerialiser


class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerialiser
    permission_classes = (KeyholderPermission, )


class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerialiser
    permission_classes = (KeyholderPermission, )


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerialiser
    permission_classes = (KeyholderPermission, )
