from django.db import models

# Create your models here.

# represents a single report
# this is created when the user uploads a photo of litter
class Report(models.Model):
    # we don't need to put id here
    # django automatically creates an id field
    picture = models.ImageField(upload_to='reports/')
    timestamp = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    