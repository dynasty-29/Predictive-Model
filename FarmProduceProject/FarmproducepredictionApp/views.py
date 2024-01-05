from django.shortcuts import render, redirect
import pandas as pd
from .models import CropPrediction
import numpy as np
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import  Response


def home(request):
    return render(request, 'home.html')


def predict(request):
    model = pd.read_pickle('plant_xgb_model.pkl')

    temperature = request.GET['temperature']
    humidity = request.GET['humidity']
    precipitation = request.GET['precipitation']
    wind_speed = request.GET['wind_speed']
    solar_radiation = request.GET['solar_radiation']
    nitrogen_level = request.GET['nitrogen_level']
    phosphorus_level = request.GET['phosphorus_level']
    potassium_level = request.GET['potassium_level']
    ph_level = request.GET['ph_level']

    lis = []

    lis.append(temperature)
    lis.append(humidity)
    lis.append(precipitation)
    lis.append(wind_speed)
    lis.append(solar_radiation)
    lis.append(nitrogen_level)
    lis.append(phosphorus_level)
    lis.append(potassium_level)
    lis.append(ph_level)

    print(lis)

    classification = model.predict([lis])

    CropPrediction.objects.create(
        temperature=temperature,
        humidity=humidity,
        precipitation=precipitation,
        wind_speed=wind_speed,
        solar_radiation=solar_radiation,
        nitrogen_level=nitrogen_level,
        phosphorus_level=phosphorus_level,
        potassium_level=potassium_level,
        ph_level=ph_level,
        classification=classification[0]
    )

    return render(request, 'predict.html', {'classification_result': classification[0]})


def db_record(request):
    crop_predictions = CropPrediction.objects.all()

    context = {
        'crop_records': crop_predictions
    }

    return render(request, 'database.html', context)


def delete(request, pk):
    crop_data = CropPrediction.objects.get(id=pk)
    crop_data.delete()
    return redirect('records')


