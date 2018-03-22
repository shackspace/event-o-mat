from rest_framework import serializers

from .models import Event, Room, Series


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

    class Meta:
        model = Event
        fields = (
            'id', 'name', 'description', 'start', 'end',
            'publish', 'room', 'series', 'keyholder',
        )
