from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Attendance, Event, Room, Series

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

    class Meta:
        model = Series
        fields = (
            'id', 'name', 'room', 'start', 'end',
        )


class EventListSerialiser(serializers.ModelSerializer):
    series = SeriesSerialiser(many=False, required=False)
    attendances = AttendanceSerialiser(many=True, read_only=True)
    modified_by = UserSerialiser(many=False)

    class Meta:
        model = Event
        fields = (
            'id', 'name', 'description', 'created', 'start', 'end',
            'publish', 'room', 'series', 'modified_by', 'modified_date', 'deleted',
            'attendances',
        )


class EventEditSerialiser(serializers.ModelSerializer):

    def validate(self, data):
        data['modified_by'] = self.context['request'].user
        return data

    class Meta:
        model = Event
        fields = (
            'id', 'name', 'description', 'start', 'end',
            'publish', 'room', 'series',
        )
