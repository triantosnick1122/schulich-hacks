from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse
from django.views.decorators import gzip

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
    cam = VideoCamera()
    frame = cam.get_frame()
    print('AAA')
    cv2.imwrite('image.jpg', frame)
    # return cam.get_frame()