import json

import pytest


@pytest.mark.django_db()
def test_room_list(room, client):
    response = client.get('/rooms/')
    assert response.status_code == 200
    content = json.loads(response.content.decode())
    assert len(content) == 1, content
    assert content[0] == {'id': room.id, 'name': room.name}
