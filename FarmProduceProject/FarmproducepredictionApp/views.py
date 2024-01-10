from django.shortcuts import render
import pandas as pd
from .models import CropPrediction
import numpy as np
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier

le = LabelEncoder()


class CropPrediction(APIView):
    def post(self, request, format=None):
        model = FarmproducepredictionappConfig.model

        # Ensure XGBoost model is an instance of XGBClassifier
        if not isinstance(model, XGBClassifier):
            return Response({"error": "Invalid model type"}, status=400)

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

        
        # Convert categorical features to numeric using LabelEncoder
        lis_encoded = [
            le.transform([value])[0] if isinstance(value, str) else value
            for value in lis
        ]

        # Print information about label encoding
        print(f"Lis: {lis}")
        print(f"Lis Encoded: {lis_encoded}")
        print(f"Label Encoder Classes: {le.classes_}")

        # Predict using the model
        classification = model.predict([lis_encoded])

        # Convert the numeric prediction back to the original crop type name
        prediction_name = le.inverse_transform([classification[0]])

        # Print information about the prediction
        print(f"Original Numeric Prediction: {classification[0]}")
        print(f"Original Categorical Prediction: {prediction_name}")

        return Response({"The best crop type to plant with these enviromental factors is": prediction_name[0]}, status=200)
