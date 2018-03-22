from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Event, Room, Series, Attendance

User = get_user_model()


class UserSerialiser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class AttendanceSerialiser(serializers.ModelSerializer):
    user = UserSerialiser(many=False)

    class Meta:
        model = Attendance
        fields = ('user', 'state')


class RoomSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = (
            'id', 'name',
        )


class SeriesSerialiser(serializers.ModelSerializer):
    room = RoomSerialiser(many=False)

    class Meta:
        model = Series
        fields = (
            'id', 'name', 'room', 'start', 'end',
        )


class EventSerialiser(serializers.ModelSerializer):
    room = RoomSerialiser(many=False)
    series = SeriesSerialiser(many=False)
    attendances = AttendanceSerialiser(many=True, read_only=True)

    class Meta:
        model = Event
        fields = (
            'id', 'name', 'description', 'start', 'end',
            'publish', 'room', 'series', 'keyholder',
            'attendances',
        )
