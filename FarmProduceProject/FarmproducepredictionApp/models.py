from django.db import models
# Create your models here.

class CropPrediction(models.Model):
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    precipitation = models.IntegerField()
    nitrogen_level = models.IntegerField()
    phosphorus_level = models.IntegerField()
    potassium_level = models.IntegerField()
    ph_level = models.IntegerField()
    crop_type = models.IntegerField()

    def __int__(self):
        return self.crop_type

# Create your models here.
