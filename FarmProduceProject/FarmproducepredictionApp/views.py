from django.shortcuts import render
import pandas as pd
from .models import CropPrediction
import numpy as np
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier

# Assuming FarmproducepredictionappConfig.model is your XGBClassifier instance
model = FarmproducepredictionappConfig.model

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
        if not isinstance(model, XGBClassifier):
            return Response({"error": "Invalid model type"}, status=400)

        temperature = request.data["temperature"]
        humidity = request.data["humidity"]
        precipitation = request.data["precipitation"]
        nitrogen_level = request.data["nitrogen_level"]
        phosphorus_level = request.data["phosphorus_level"]
        potassium_level = request.data["potassium_level"]
        ph_level = request.data["ph_level"]

        lis = [
            temperature,
            humidity,
            precipitation,
            nitrogen_level,
            phosphorus_level,
            potassium_level,
            ph_level,
        ]

        # Convert categorical features to numeric using LabelEncoder
        lis_encoded = [
            le.transform([value])[0] if isinstance(value, str) else value
            for value in lis
        ]

        # Inverse transform for categorical features
        lis_encoded = [
            le.inverse_transform([value])[0] if isinstance(value, int) else value
            for value in lis_encoded
        ]

        # Print information about label encoding
        print(f"Lis: {lis}")
        print(f"Lis Encoded: {lis_encoded}")
        print(f"Label Encoder Classes: {le.classes_}")

        # Predict using the model
        classification = model.predict([lis_encoded])

        try:
        # Convert the numeric prediction back to the original crop type name
            prediction_name = le.inverse_transform([classification[0]])
        except ValueError as e:
        # Handle the case of an unseen label, you can provide a default value or take appropriate action
            prediction_name = "Unknown Label"
        print(f"Warning: Unseen label encountered - {e}")

        # Print information about the prediction
        print(f"Original Numeric Prediction: {classification[0]}")
        print(f"Original Categorical Prediction: {prediction_name}")
