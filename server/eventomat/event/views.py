from rest_framework import status, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .models import Attendance, Event, Room, Series
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

    @detail_route(methods=['post'])
    def attend(self, request, pk):
        event = self.get_object()
        state = request.POST.get('state', 'yes')
        if state not in ('yes', 'no', 'maybe'):
            return Response(
                'Status must be yes, no, or maybe, not {state}.'.format(state),
                status=status.HTTP_400_BAD_REQUEST,
            )
        if request.user.is_anonymous:
            return Response(
                'User must not be anonymous.',
                status=status.HTTP_400_BAD_REQUEST,
            )
        Attendance.objects.get_or_create(event=event, user=request.user, defaults={'state': state})
        return Response(status=status.HTTP_200_OK)
