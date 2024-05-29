import logging

from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View

from .models import Garden, GardenBed, Plant


class GardenListView(ListView):
    model = Garden
    template_name = "garden_list.html"


class GardenDetailView(View):
    # dartmouth = GardenBed.objects.get(garden_id=)
    # dartmouth.student_set.all()  # returns all students at Dartmouth
    # dartmouth.objects.filter(student__first_name='william')  # returns all Dartmouth students named William

    def get(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        garden = Garden.objects.get(pk=pk)
        beds = GardenBed.objects.filter(garden=garden)
        return render(request, "garden_detail.html", {"garden": garden, "beds": beds})
