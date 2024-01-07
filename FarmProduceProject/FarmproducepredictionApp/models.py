from django.db import models
# Create your models here.

class CropPrediction(models.Model):
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    precipitation = models.IntegerField()
    wind_speed = models.IntegerField()
    solar_radiation = models.IntegerField()
    nitrogen_level = models.IntegerField()
    phosphorus_level = models.IntegerField()
    potassium_level = models.IntegerField()
    ph_level = models.IntegerField()
    classification = models.IntegerField()

    def __str__(self):  # Change __int__ to __str__
        return str(self.classification)
