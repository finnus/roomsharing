from factory import Faker, Sequence
from factory.django import DjangoModelFactory

from roomsharing.rs_organizations.models import Organization


class OrganizationFactory(DjangoModelFactory):
    class Meta:
        model = Organization

    name = Sequence(lambda n: "Organization%d" % n)
    description = Faker("sentence", nb_words=10)
    email = Faker("email")
    phone = Faker("phone_number")
    contact_person = Faker("name")
    website = Faker("url")
