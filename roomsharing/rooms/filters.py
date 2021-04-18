import django_filters
from django.utils.translation import gettext_lazy as _

from roomsharing.rs_organizations.models import Organization

from .models import Amenity, Aptitude, Room


class RoomFilter(django_filters.FilterSet):
    aptitudes = django_filters.ModelMultipleChoiceFilter(
        field_name="roomaptitude_of_room__aptitude__name",
        to_field_name="name",
        lookup_expr="contains",
        queryset=Aptitude.objects.all(),
        label=_("Aptitudes"),
    )
    amenities = django_filters.ModelMultipleChoiceFilter(
        field_name="roomamenity_of_room__amenity__name",
        to_field_name="name",
        lookup_expr="contains",
        queryset=Amenity.objects.all(),
        label=_("Amenities"),
    )
    persons = django_filters.NumberFilter(method="persons_filter", label=_("Persons"))
    organization = django_filters.ModelChoiceFilter(
        field_name="organization",
        to_field_name="slug",
        queryset=Organization.objects.all(),
        label=_("Organization"),
    )

    class Meta:
        model = Room
        fields = [
            "square_meters",
            "organization",
            "aptitudes",
            "amenities",
            "persons",
        ]

    def persons_filter(self, queryset, name, value):
        return Room.objects.filter(capacity_from__lte=value + 3).filter(
            capacity_to__gte=value - 3
        )
