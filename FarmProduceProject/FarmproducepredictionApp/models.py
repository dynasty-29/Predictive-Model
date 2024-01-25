from typing import Any
from django.db import models


# crop prediction model
class CropPrediction(models.Model):
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    precipitation = models.IntegerField()
    nitrogen_level = models.IntegerField()
    phosphorus_level = models.IntegerField()
    potassium_level = models.IntegerField()
    ph_level = models.IntegerField()
    classification = models.CharField(max_length=50)

    def __int__(self):
        return self.classification


# animal produce model
class AnimPrediction(models.Model):
    nutrition_protein = models.IntegerField()
    nutrition_carbohydrates = models.IntegerField()
    nutrition_minerals = models.IntegerField()
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    prev_milk_production = models.IntegerField()
    predicted_milk_production = models.IntegerField()
    
    def __init__(self):
        return self.predicted_milk_production