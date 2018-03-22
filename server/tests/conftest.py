import pytest

from eventomat.event.models import Room


@pytest.fixture
def room():
    return Room.objects.create(name='The Rom')
