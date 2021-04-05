import pytest

from roomsharing.rooms.tests.factories import RoomFactory

pytestmark = pytest.mark.django_db


def test_room__str__():
    r = RoomFactory()
    assert r.__str__() == r.name


def test_room_get_absolute_url():
    r = RoomFactory()
    assert r.get_absolute_url() == f"/rooms/{r.slug}/"
