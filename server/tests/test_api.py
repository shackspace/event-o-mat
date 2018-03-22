import json
from datetime import timedelta

import pytest
import pytz
from django.utils.timezone import now

from eventomat.event.models import Event


@pytest.mark.django_db()
def test_room_list(room, client):
    response = client.get('/rooms/')
    assert response.status_code == 200
    content = json.loads(response.content.decode())
    assert len(content) == 1, content
    assert content[0] == {
        'id': room.id,
        'name': room.name,
    }


@pytest.mark.django_db()
def test_event_list(event_with_series, client, attendance):
    event = event_with_series
    response = client.get('/events/')
    assert response.status_code == 200
    content = json.loads(response.content.decode())
    assert len(content) == 1, content
    assert content[0] == {
        'id': event.id,
        'name': event.name,
        'description': event.description,
        'start': event.start.astimezone(pytz.timezone('Europe/Berlin')).isoformat(),
        'end': event.end.astimezone(pytz.timezone('Europe/Berlin')).isoformat(),
        'publish': event.publish,
        'series': {'id': event.series.id, 'name': event.series.name, 'room': None, 'start': None, 'end': None},
        'keyholder': event.keyholder.id,
        'room': {'id': event.room.id, 'name': event.room.name},
        'attendances': [
            {
                'user': {'username': attendance.user.username, 'id': attendance.user.id},
                'state': attendance.state,
            }
        ]
    }


@pytest.mark.django_db()
def test_series_list(series, client):
    response = client.get('/series/')
    assert response.status_code == 200
    content = json.loads(response.content.decode())
    assert len(content) == 1, content
    assert content[0] == {
        'id': series.id,
        'name': series.name,
        'start': None,
        'end': None,
        'room': None,
    }


@pytest.mark.django_db()
def test_create_event(client, room, keyholder_user):
    count = Event.objects.count()
    event_data = {
        'name': 'Teh Event',
        'start': (now() + timedelta(days=1)).isoformat(),
        'end': (now() + timedelta(hours=25)).isoformat(),
        'publish': True,
        'room': room.id,
    }
    response = client.post('/events/', data=event_data)
    assert response.status_code == 401
    client.force_login(keyholder_user)
    response = client.post('/events/', data=event_data)
    assert response.status_code == 201, response.content.decode()
    assert Event.objects.count() == count + 1
