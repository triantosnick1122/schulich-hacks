from django.test import TestCase
from Trashporter.models import Report
import os
import urllib.request
from datetime import datetime
import geocoder
import ssl
import os
import random
from django.core.files import File


ssl._create_default_https_context = ssl._create_unverified_context

# Create your tests here.

class PictureTestCase(TestCase):
    def setUp(self):
        pass

    # make sure that the pictures are actually being saved in db
    def test_picture_saving(self):

        filenameShorthand = "~/Desktop/testPics.jpg"
        filename = os.path.expanduser(filenameShorthand)

        # delete the file if it exists
        if os.path.exists(filename):
            os.remove(filename)

        # create a new report object with some dummy data
        # this is a valid image url
        picUrl = "https://farm66.staticflickr.com/65535/33978196618_632623b4fc_z.jpg"
        # get current time
        now = datetime.now()
        # get lat and long using geocoder
        g = geocoder.ip('me')
        long = g.lng
        lat = g.lat

        print ('attempting to download image from url: ' + picUrl)
        # download the pic from url so we can use it in report
        pic = urllib.request.urlopen(picUrl)
        # turn into a file
        picFile = File(pic)

        # create a new report object
        created = Report(picture=picFile, timestamp=now, latitude=lat, longitude=long)

        # save the report object to the database
        created.save()

        # now there should be one report in the db. grab it
        report = Report.objects.get()

        # grab the picture from the report
        picture = report.picture

        # picture should be a Django ImageFile
        # check that it is
        self.assertTrue(isinstance(picture, File))
        # now take the content of it and save to '/Desktop/testPics.jpg'
        # this is the same as the picture that was uploaded

        # at this point, the file with path filename should not exist
        self.assertFalse(os.path.exists(filename))

        # create the file
        open(filename, 'a').close()
        # open the file and write the picture to it
        f = open(filename, 'wb')
        f.write(picture.read())
        # close the file
        f.close()

        # now check that the file exists
        self.assertTrue(os.path.exists(filename))
