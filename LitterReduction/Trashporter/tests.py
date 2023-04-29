from django.core.files.storage import default_storage
from django.core.files import File
from django.test import TestCase
from django.utils import timezone
from .models import Report
from datetime import datetime
import geocoder
import os
import urllib.request
import ssl

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
