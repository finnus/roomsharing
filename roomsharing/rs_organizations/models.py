from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from organizations.abstract import (
    AbstractOrganization,
    AbstractOrganizationInvitation,
    AbstractOrganizationOwner,
    AbstractOrganizationUser,
)


class Organization(AbstractOrganization):
    name = models.CharField(_("Name"), max_length=200)
    description = models.TextField(_("Description"), max_length=4000)
    email = models.EmailField(_("E-Mail"), null=False, blank=False)
    phone = models.CharField(_("Telephone"), max_length=200, null=True, blank=True)
    contact_person = models.CharField(
        _("Contact Person"), max_length=200, null=True, blank=True
    )
    website = models.URLField(_("Website"), max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("organizations:detail", kwargs={"slug": self.slug})


class OrganizationOwner(AbstractOrganizationOwner):
    pass


class OrganizationUser(AbstractOrganizationUser):
    pass


class OrganizationInvitation(AbstractOrganizationInvitation):
    pass


class OrganizationalAddress(models.Model):
    class Country(models.IntegerChoices):
        GERMANY = 1, _("Germany")

    additional_address_line = models.CharField(
        _("Additional Address Line"), max_length=200, null=True, blank=True
    )
    street = models.CharField(_("Street"), max_length=200, null=True, blank=True)
    building_number = models.CharField(
        _("Building Number"), max_length=200, null=True, blank=True
    )
    postal_code = models.CharField(
        _("Postal Code"), max_length=200, null=True, blank=True
    )
    city = models.CharField(_("City"), max_length=200, null=True, blank=True)
    country = models.IntegerField(
        _("Country"), choices=Country.choices, default=Country.GERMANY
    )
    long = models.DecimalField(
        _("Longitude"), max_digits=9, decimal_places=6, null=True, blank=True
    )
    lat = models.DecimalField(
        _("Latitude"), max_digits=9, decimal_places=6, null=True, blank=True
    )
    organization = models.ForeignKey(
        Organization,
        related_name="organizationaladdresses_of_organization",
        related_query_name="organizationaladdress_of_organization",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return (
            self.street
            + " "
            + self.building_number
            + ", "
            + self.postal_code
            + " "
            + self.city
        )
