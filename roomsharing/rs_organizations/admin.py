from django.contrib import admin
from organizations.base_admin import (
    BaseOrganizationAdmin,
    BaseOrganizationOwnerAdmin,
    BaseOrganizationUserAdmin,
    BaseOwnerInline,
)

from .models import Organization, OrganizationOwner, OrganizationUser


class OwnerInline(BaseOwnerInline):
    model = OrganizationOwner


class OrganizationAdmin(BaseOrganizationAdmin):
    inlines = [OwnerInline]


class OrganizationUserAdmin(BaseOrganizationUserAdmin):
    pass


class OrganizationOwnerAdmin(BaseOrganizationOwnerAdmin):
    pass


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(OrganizationUser, OrganizationUserAdmin)
admin.site.register(OrganizationOwner, OrganizationOwnerAdmin)
