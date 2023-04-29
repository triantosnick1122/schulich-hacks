from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse
from django.views.decorators import gzip
from .models import Report
from Trashporter.camera import *

def index(request):
    return render(request, "index.html")

def camera_feed(request):
    return render(request, "camera.html")

@gzip.gzip_page
def camera(request):
    cam = VideoCamera()
    return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")

def capture_img(request):
    latitude = float(request.GET["latitude"])
    longitude = float(request.GET["longitude"])
    print(latitude,longitude)
    frame = VideoCamera().frame
    cv2.imwrite('image.jpg', frame)
    report = Report(picture=frame, latitude=latitude, longitude=longitude)
    report.save()
    return HttpResponse(status=200)