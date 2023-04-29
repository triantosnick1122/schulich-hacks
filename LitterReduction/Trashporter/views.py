from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse
from django.views.decorators import gzip
from .models import Report
from Trashporter.camera import *
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

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
    #cv2.imwrite('image.jpg', frame)
    #frame = cv2.imread("C:/Users/edgar/Desktop/SchulichHacks/schulich-hacks/LitterReduction/image.jpg")
    _, frame_jpg = cv2.imencode('.jpg', frame)
    file = ContentFile(frame_jpg.tobytes())
    report = Report(latitude=latitude, longitude=longitude)
    report.picture.save('output.jpg', file)
    report.save()
    # instance = Report.objects.get(id=14)
    # imfield = instance.picture.open()
    # img = cv2.imread(imfield.name)
    return HttpResponse(status=200)