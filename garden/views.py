from django.views.generic import DetailView, ListView

from .models import Garden, GardenBed, Plant


class GardenListView(ListView):
    model = Garden
    template_name = "garden_list.html"


class GardenDetailView(DetailView):
    model = GardenBed
    template_name = "garden_detail.html"
