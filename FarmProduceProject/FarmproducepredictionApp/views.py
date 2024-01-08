from django.shortcuts import render, redirect
import pandas as pd
from .models import CropPrediction
import numpy as np
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()


class CropPrediction(APIView):
    def post(self, request, format=None):
        model = FarmproducepredictionappConfig.model
        temperature = request.data["temperature"]
        humidity = request.data["humidity"]
        precipitation = request.data["precipitation"]
        wind_speed = request.data["wind_speed"]
        solar_radiation = request.data["solar_radiation"]
        nitrogen_level = request.data["nitrogen_level"]
        phosphorus_level = request.data["phosphorus_level"]
        potassium_level = request.data["potassium_level"]
        ph_level = request.data["ph_level"]

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

        # Convert the numeric prediction back to the original crop type name
        prediction_name = le.inverse_transform([classification[0]])[0]

        return Response({"classification_result": prediction_name}, status=200)
