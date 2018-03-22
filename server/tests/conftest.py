from datetime import timedelta

import pytest
from django.contrib.auth import get_user_model
from django.utils.timezone import now

from eventomat.event.models import Attendance, Event, Room, Series


@pytest.fixture
def keyholder_user():
    return get_user_model().objects.create(username='keyholderrr', is_staff=True)


@pytest.fixture
def regular_user():
    return get_user_model().objects.create(username='normalo')


@pytest.fixture
def room():
    return Room.objects.create(name='The Rom')


@pytest.fixture
def series():
    return Series.objects.create(name='Best series')


@pytest.fixture
def event_without_series(room, keyholder_user):
    return Event.objects.create(
        name='Teh Event',
        start=now() + timedelta(days=1),
        end=now() + timedelta(hours=25),
        publish=True,
        keyholder=keyholder_user,
        room=room
    )


@pytest.fixture
def event_with_series(room, keyholder_user, series):
    return Event.objects.create(
        name='Teh Event',
        start=now() + timedelta(days=1),
        end=now() + timedelta(hours=25),
        publish=True,
        keyholder=keyholder_user,
        series=series,
        room=room
    )


@pytest.fixture()
def attendance(event_with_series, regular_user):
    return Attendance.objects.create(user=regular_user, event=event_with_series, state='yes')
