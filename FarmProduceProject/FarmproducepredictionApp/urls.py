from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FarmproducepredictionApp.urls')),
    path('', CropPrediction.as_view(), name = 'prediction ')
]