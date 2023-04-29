from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("litter_map/", views.litter_map, name="litter_map"),
]