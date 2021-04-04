from django.views.generic import DetailView, ListView

from .models import Organization


class OrganizationListView(ListView):
    model = Organization


organization_list_view = OrganizationListView.as_view()


class OrganizationDetailView(DetailView):
    model = Organization


organization_detail_view = OrganizationDetailView.as_view()
