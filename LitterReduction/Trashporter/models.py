from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

# represents a single report
# this is created when the user uploads a photo of litter
class Report(models.Model):

    class LitterType(models.TextChoices):
        PLASTIC = 'Plastic', _('Plastic')
        FURNITURE = 'Furniture', _('Furniture')
        METAL = 'Metal', _('Metal')
        FOOD = 'Food', _('Food')
        DANGEROUS = 'Dangerous', _('Dangerous')
        OTHER = 'Other', _('Other')
        GLASS = 'Glass', _('Glass')
        NONE = 'None', _('None')

    class LitterQuantity(models.TextChoices):
        LOW = 'Low', _('Low')
        MEDIUM = 'Medium', _('Medium')
        LARGE = 'Large', _('Large')
        NONE = 'None', _('None')

    picture = models.ImageField(upload_to='reports/')
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    type_tag = models.CharField(max_length=15, choices=LitterType.choices, default=LitterType.NONE)
    quantity_tag = models.CharField(max_length=15, choices=LitterQuantity.choices, default=LitterQuantity.NONE)
    extra_description = models.CharField(max_length=100, default="")

    def get_litter_type(self) -> LitterType:
        return self.LitterType[self.type_tag]
    
    def get_litter_quantity(self) -> LitterQuantity:
        return self.LitterQuantity[self.quantity_tag]

    # override Django default behavior of appending app name to table name
    # class Meta:
    #     db_table = 'report'
