from factory import Faker, Sequence, SubFactory
from factory.django import DjangoModelFactory

from roomsharing.rs_organizations.models import Organization, OrganizationalAddress


class OrganizationFactory(DjangoModelFactory):
    class Meta:
        model = Organization

    name = Sequence(lambda n: "Organization%d" % n)
    description = Faker("sentence", nb_words=10)
    email = Faker("email")
    phone = Faker("phone_number")
    contact_person = Faker("name")
    website = Faker("url")


class OrganizationalAddressFactory(DjangoModelFactory):
    class Meta:
        model = OrganizationalAddress

    additional_address_line = Faker("street_suffix")
    street = Faker("street_name")
    building_number = Faker("building_number")
    postal_code = Faker("postcode")
    city = Faker("city")
    country = 1
    long = Faker("longitude")
    lat = Faker("latitude")
    organization = SubFactory(OrganizationFactory)
