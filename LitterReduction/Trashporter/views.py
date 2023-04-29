from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import HttpResponse,StreamingHttpResponse
from django.views.decorators import gzip
from .models import Report
from Trashporter.camera import *
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

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
    print('Capturing image and making a report...')
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
    print('Report saved!')
    # instance = Report.objects.get(id=14)
    # imfield = instance.picture.open()
    # img = cv2.imread(imfield.name)
    return HttpResponse(status=200)

# get all reports from db and return them as json array
def get_reports():
    reports = Report.objects.all()
    reports_json = []
    for report in reports:
        reports_json.append({
            "latitude": report.latitude,
            "longitude": report.longitude,
            "type_tag": report.type_tag,
            "quantity_tag": report.quantity_tag,
            "extra_description": report.extra_description,
            "timestamp": report.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "picture": report.picture.url
        })
    return reports_json

# turn the list of reports into our preferred format
def format_reports():
    # take the list of reports
    reports = get_reports()
    # generate a list of latitude-longitude tuples
    locations = []
    # also type_tags
    type_tags = []
    # so on and so forth
    quantity_tags = []
    extra_descriptions = []
    timestamps = []
    pictures = []

    # build the lists
    for report in reports:
        locations.append((report['latitude'], report['longitude']))
        type_tags.append(report['type_tag'])
        quantity_tags.append(report['quantity_tag'])
        extra_descriptions.append(report['extra_description'])
        timestamps.append(report['timestamp'])
        pictures.append(report['picture'])

    return locations, type_tags, quantity_tags, extra_descriptions, timestamps, pictures    

