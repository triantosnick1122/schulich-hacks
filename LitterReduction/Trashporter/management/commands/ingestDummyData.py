from django.core.management.base import BaseCommand, CommandError
from Trashporter.models import Report
import sys
import csv
import urllib.request
import ssl
import os
import random
from django.core.files import File
from datetime import datetime, timedelta


ssl._create_default_https_context = ssl._create_unverified_context

class Command(BaseCommand):
    help = "Load some dummy report data."

    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str)

    def handle(self, *args, **options):

        print(options)

        # open the csv file
        csv_file = open(options["csv_path"])

        # the csv file has 2 records per line, so make sure to iterate by comma not by line
        reader = csv.reader(csv_file, delimiter=",")
        next(reader)

        # iterate through the csv file
        for row in reader:
            try:
                # grab the link from this row
                link = row[0]
                # download the image at the link
                print('Attempting to download from ' + link)
                image = urllib.request.urlopen(link)

                # randomly generated fields
                # set the timestamp to some random time between now and 30 days ago
                # generate a random datetime from between now and 90 days ago
                randtime = datetime.now() - timedelta(days=random.randint(0, 90))
                print ('Timestamp is: ' + str(randtime))
                # set the latitude and longitude to some random location in the continental US or Canada
                randlat = random.uniform(30, 50)
                randlong = random.uniform(-120, -70)

                # turn the image into a django File object
                imageFile = File(image)



                # create a new report object
                # create the object and give the field values all at once
                report = Report(picture=imageFile, timestamp=randtime, latitude=randlat, longitude=randlong)

                
                # save the report object to the database
                report.save()
                print('success!')

            except Exception as e:
                print('error.')    
                print(e)

        # close the file
        csv_file.close()        
