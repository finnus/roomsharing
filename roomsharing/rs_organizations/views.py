from django.views.generic import ListView

from .models import Organization


class OrganizationListView(ListView):
    model = Organization


organization_list_view = OrganizationListView.as_view()
