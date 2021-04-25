from factory import Faker, Sequence, SubFactory
from factory.django import DjangoModelFactory

from roomsharing.rooms.models import Room
from roomsharing.rs_organizations.tests.factories import (
    OrganizationalAddressFactory,
    OrganizationFactory,
)


class RoomFactory(DjangoModelFactory):
    class Meta:
        model = Room

    organization = SubFactory(OrganizationFactory)
    name = Sequence(lambda n: "Room%d" % n)
    description = Faker("sentence", nb_words=10)
    capacity_from = 5
    capacity_to = 15
    square_meters = 20
    rules = Faker("sentence", nb_words=10)
    published = True
    address = SubFactory(OrganizationalAddressFactory)
