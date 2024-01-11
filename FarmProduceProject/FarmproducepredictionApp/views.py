from django.shortcuts import render
import pandas as pd
from .models import CropPrediction, AnimPrediction
import numpy as np
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier, XGBRegressor

# Assuming FarmproducepredictionappConfig.model is your XGBClassifier instance
model1 = FarmproducepredictionappConfig.model1

# Define your class mapping
class_mapping = {
    0: "apple",
    1: "banana",
    2: "blackgram",
    3: "chickpea",
    4: "coconut",
    5: "coffee",
    6: "cotton",
    7: "grapes",
    8: "jute",
    9: "kidneybeans",
    10: "lentil",
    11: "maize",
    12: "mango",
    13: "mothbeans",
    14: "mungbean",
    15: "muskmelon",
    16: "orange",
    17: "papaya",
    18: "pigeonpeas",
    19: "pomegranate",
    20: "rice",
    21: "watermelon",
}

# Extract labels from class_mapping
your_training_data_labels = list(class_mapping.values())

# Fit the LabelEncoder on your data
le = LabelEncoder()
le.fit(your_training_data_labels)


class CropPrediction(APIView):
    def post(self, request, format=None):
        # Ensure XGBoost model is an instance of XGBClassifier
        if not isinstance(model1, XGBClassifier):
            return Response({"error": "Invalid data"}, status=400)

        temperature = request.data["temperature"]
        humidity = request.data["humidity"]
        precipitation = request.data["precipitation"]
        nitrogen_level = request.data["nitrogen_level"]
        phosphorus_level = request.data["phosphorus_level"]
        potassium_level = request.data["potassium_level"]
        ph_level = request.data["ph_level"]

        lis = [
            nitrogen_level,
            phosphorus_level,
            potassium_level,
            temperature,
            humidity,
            ph_level,
            precipitation,
        ]

        # Convert categorical features to numeric using LabelEncoder
        lis_encoded = [
            le.transform([value])[0] if isinstance(value, str) else value
            for value in lis
        ]

        # Predict using the model
        classification = model1.predict([lis])

        predicted_crop_type = class_mapping[int(classification[0])]

        # Return the prediction result in the response
        return Response(
            {"The best crop to farm with these conditions is": predicted_crop_type},
            status=200,
        )


class AnimPrediction(APIView):
    def post(self, request, format=None):
        # Ensure XGBoost model is an instance of XGBRegressor
        if not isinstance(model2, XGBRegressor):
            return Response({"error": "Invalid data"}, status=400)

        breed = request.data["breed"]
        health_status = request.data["health_status"]
        lactation_stage = request.data["lactation_stage"]
        reproductive_status = request.data["reproductive_status"]
        milking_frequency = request.data["milking_frequency"]
        age = request.data["age"]
        nutrition_protein = request.data["nutrition_protein"]
        nutrition_carbohydrates = request.data["nutrition_carbohydrates"]
        nutrition_minerals = request.data["nutrition_minerals"]
        temperature = request.data["temperature"]
        humidity = request.data["humidity"]
        prev_milk_production = request.data["prev_milk_production"]

        lis2 = [
            breed,
            health_status,
            lactation_stage,
            reproductive_status,
            milking_frequency,
            age,
            nutrition_protein,
            temperature,
            humidity,
            nutrition_carbohydrates,
            nutrition_minerals,
            prev_milk_production,
        ]

        # Convert categorical features to numeric using LabelEncoder
        # lis_encoded = [
        #     le.transform([value])[0] if isinstance(value, str) else value
        #     for value in lis2
        # ]

        # Predict using the model2
        predicted_milk_production = model2.predict([lis2])

        # predicted_milk_production_ = class_mapping[int(predicted_milk_production[0])]

        # Return the prediction result in the response
        return Response(
            {"The expected milk production is": predicted_milk_production}, status=200
        )
