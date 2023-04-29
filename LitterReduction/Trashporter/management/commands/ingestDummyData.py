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
        parser.add_argument("csv_folder", type=str)

    def handle(self, *args, **options):

        print(options)

        # open the csv files
        # image links file will be in csv_folder/image_links.csv
        image_links_file = open(os.path.join(options["csv_folder"], "image_links.csv"))
        # sample comments file in same folder with filename sample_comments.csv
        sample_comments_file = open(os.path.join(options["csv_folder"], "sample_comments.csv"))

        # the image links csv file has 2 records per line, so make sure to iterate by comma not by line
        links_reader = csv.reader(image_links_file, delimiter=",")
        next(links_reader)

        # comments csv file
        comments_reader = csv.reader(sample_comments_file, delimiter=",")
        next(comments_reader)

        # iterate through the csv file of links
        for row in links_reader:
            try:
                # grab the link from this row
                link = row[0]
                # download the image at the link
                # print('Attempting to download from ' + link)
                image = urllib.request.urlopen(link)

                # now grab the comment from the current row of comments file
                # if there are no more records left in the comments file, just stop the outer loop.
                try:
                    comment = next(comments_reader)[0]
                except StopIteration:
                    break


                # randomly generated fields
                # set the timestamp to some random time between now and 30 days ago
                # generate a random datetime from between now and 90 days ago
                randtime = datetime.now() - timedelta(days=random.randint(0, 90))
                # print ('Timestamp is: ' + str(randtime))
                # set the latitude and longitude to some random location in the continental US or Canada
                randlat = random.uniform(30, 50)
                randlong = random.uniform(-120, -70)
                # set the type_tag to a random value
                type_tags = ['PL', 'FU', 'ME', 'FO', 'DA', 'OT', 'GL', 'NO']
                randtag = random.choice(type_tags)
                # set the quantity tag to a random value
                quantity_tags = ['LOW', 'MED', 'LRG', 'NON']
                randquant = random.choice(quantity_tags)


                # turn the image into a django File object
                # we'll save it in reports folder
                # the name will be extracted from the link (there's a filename in it.)
                filename = os.path.basename(link)

                imageFile = File(image, name=filename)

                print('name of the saved file is ' + str(imageFile.name))



                # create a new report object
                # create the object and give the field values all at once
                report = Report(picture=imageFile, timestamp=randtime, latitude=randlat, longitude=randlong, extra_description=comment, type_tag=randtag, quantity_tag=randquant)

                
                # save the report object to the database
                report.save()
                print('success! report has been saved.')
                print(report)

            except Exception as e:
                print('error.')    
                print(e)

        # close the file
        image_links_file.close()     
        sample_comments_file.close()   
