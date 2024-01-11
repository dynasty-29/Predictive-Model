from django.contrib import admin
from django.urls import path, include
from .views import CropPrediction, AnimPrediction


urlpatterns = [
    path('crop-prediction', CropPrediction.as_view(), name = 'cropprediction '),
    path('animal-prediction/', AnimPrediction.as_view(), name = 'animprediction'),
]