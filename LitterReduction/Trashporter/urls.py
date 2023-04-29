from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("camera_feed/",views.camera_feed, name="camera_feed"),
    path("camera/",views.camera, name="live_camera")
]