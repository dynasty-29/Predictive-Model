from django.contrib import admin
from django.urls import path, include
from .views import CropPrediction


urlpatterns = [
    path('crop-prediction', CropPrediction.as_view(), name = 'prediction ')
]