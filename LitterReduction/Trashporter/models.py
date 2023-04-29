from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

# represents a single report
# this is created when the user uploads a photo of litter
class Report(models.Model):

    class LitterType(models.TextChoices):
        PLASTIC = 'PL', _('Plastic')
        FURNITURE = 'FU', _('Furniture')
        METAL = 'ME', _('Metal')
        FOOD = 'FO', _('Food')
        DANGEROUS = 'DA', _('Dangerous')
        OTHER = 'OT', _('Other')
        GLASS = 'GL', _('Glass')
        NONE = 'NO', _('None')

    class LitterQuantity(models.TextChoices):
        LOW = 'LOW', _('Low')
        MEDIUM = 'MED', _('Medium')
        LARGE = 'LRG', _('Large')
        NONE = 'NON', _('None')

    picture = models.ImageField(upload_to='reports/')
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    type_tag = models.CharField(max_length=2, choices=LitterType.choices, default=LitterType.NONE)
    quantity_tag = models.CharField(max_length=3, choices=LitterQuantity.choices, default=LitterQuantity.NONE)
    extra_description = models.CharField(max_length=100, default="")

    def get_litter_type(self) -> LitterType:
        return self.LitterType[self.type_tag]
    
    def get_litter_quantity(self) -> LitterQuantity:
        return self.LitterQuantity[self.quantity_tag]

    # override Django default behavior of appending app name to table name
    class Meta:
        db_table = 'report'
