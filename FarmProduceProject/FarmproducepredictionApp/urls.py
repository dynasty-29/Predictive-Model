from django.contrib import admin
from django.urls import path, include
from .views import *
from .views import predict_croptype


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FarmproducepredictionApp.urls')),
    path('', predict_croptype.as_view(), name = 'prediction ')
]