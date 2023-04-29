from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import HttpResponse,StreamingHttpResponse
from django.views.decorators import gzip

from Trashporter.camera import *

def index(request):
    return render(request, "index.html")

def litter_map(request): 
    # Your code to retrieve the location and other data goes here
    locations = [(30.5, 50.5), (30.55, 50.6)]
    garbage_amounts = ["small", "large"]
    garbage_types = ["plastic", "metal"]
    other_comments = ["This is a description of the location", "second description"]

    
    return render(request, 'map.html', {'locations': json.dumps(locations), 'other_comments': json.dumps(other_comments), 
                                        'garbage_types': json.dumps(garbage_types), 'garbage_amounts': json.dumps(garbage_amounts)})
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
    return HttpResponse(status=200)
