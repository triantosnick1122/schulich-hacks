from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("litter_map/", views.litter_map, name="litter_map"),
    path("camera_feed/",views.camera_feed, name="camera_feed"),
    path("camera/",views.camera, name="live_camera"),
    path("capture_img",views.capture_img, name = "capture_img"),
    path("get_reports",views.get_reports, name = "get_reports")
]
