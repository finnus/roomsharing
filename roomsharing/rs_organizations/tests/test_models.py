import pytest

from roomsharing.rs_organizations.tests.factories import OrganizationFactory

pytestmark = pytest.mark.django_db


def test_organization__str__():
    o = OrganizationFactory()
    assert o.__str__() == o.name


def test_organization_get_absolute_url():
    o = OrganizationFactory()
    assert o.get_absolute_url() == f"/organizations/{o.pk}/"
