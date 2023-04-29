from django.core.files.storage import default_storage
from django.core.files import File
from django.test import TestCase
from django.utils import timezone
from .views import format_reports
from .models import Report
from datetime import datetime
import geocoder
import os
import urllib.request
import ssl
import csv
import random


# ignore certificates
ssl._create_default_https_context = ssl._create_unverified_context

class PictureTestCase(TestCase):
    def setUp(self):
        pass

    def test_picture_saving(self):
        filenameShorthand = "~/Desktop/testPics.jpg"
        filename = os.path.expanduser(filenameShorthand)

        if os.path.exists(filename):
            os.remove(filename)

        picUrl = "https://farm66.staticflickr.com/65535/33978196618_632623b4fc_z.jpg"
        now = datetime.now()
        g = geocoder.ip('me')
        long = g.lng
        lat = g.lat

        print ('attempting to download image from url: ' + picUrl)
        pic = urllib.request.urlopen(picUrl)
        print('type of pic: ' + str(type(pic)))
        print('url of pic: ' + str(pic.url))

        # there is a filename in the url--extract it
        picFileName = os.path.basename(picUrl)
        picFile = File(pic, name=picFileName)

        # Create a new Report object with some dummy data and save it to the database
        created = Report(picture=picFile, timestamp=now, latitude=lat, longitude=long)
        created.save()

        # Retrieve the Report object from the database
        report = Report.objects.get()

        # Get the content of the ImageFile
        print('name of the picture is ' + str(report.picture.name))
        content = default_storage.open(report.picture.name, 'rb').read()

        # Save the content to the specified file
        with open(os.path.join(filename), 'wb') as f:
            f.write(content)

        # Assert that the file exists
        self.assertTrue(os.path.exists(filename))

    def test_format_reports(self):
        print('testing get_reports()...')
        
        # create 1000 dummy reports and save them to the database
        # use the image links from the csv to get images

        # read from the csv file in data and make a list of the image links
        csv_file = open('../data/image_links.csv')
        reader = csv.reader(csv_file, delimiter=",")
        next(reader)
        links = []
        for row in reader:
            links.append(row[0])


        for i in range(64):
            now = datetime.now()
            g = geocoder.ip('me')
            long = g.lng
            lat = g.lat
            # get the next image link from the list
            link = links[i]

            # download the image at the link
            print('Attempting to download from ' + link)
            image = urllib.request.urlopen(link)
            # turn the image into a django File object
            # we'll save it in reports folder
            # the name will be extracted from the link (there's a filename in it.)
            filename = os.path.basename(link)
            imageFile = File(image, name=filename)
            print('name of the saved file is ' + str(imageFile.name))
            # create a new report object
            # create the object and give the field values all at once
            created = Report(picture=imageFile, timestamp=now, latitude=lat, longitude=long)
            created.save()

        # now call views.format_reports and print
        reports = format_reports()
        print(reports)