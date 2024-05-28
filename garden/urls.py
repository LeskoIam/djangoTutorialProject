# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

from django.urls import path

from .views import GardenListView, GardenDetailView

urlpatterns = [
    path("<int:pk>/", GardenDetailView.as_view(), name="garden_detail"),
    path("", GardenListView.as_view(), name="garden_list"),
]
