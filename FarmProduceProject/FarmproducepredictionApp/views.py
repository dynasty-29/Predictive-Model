from django.shortcuts import render
import pandas as pd
from .models import CropPrediction, AnimPrediction
import numpy as np
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.linear_model import LinearRegression

# Assuming FarmproducepredictionappConfig.model is your XGBClassifier instance
model1 = FarmproducepredictionappConfig.model1
grid_search_model = FarmproducepredictionappConfig.model2
model2 = grid_search_model
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
        classification = model1.predict([lis_encoded])
        print(classification)
        # crops = []
        # for i in classification:
        #     predicted_crop_type = class_mapping[int(i)]
        #     crops.append(predicted_crop_type)

        crops = [class_mapping[int(i)] for i in classification]

        # Return the prediction result in the response
        return Response(
            {"The best crop to farm with these conditions is": crops},
            status=200,
        )


# Define a default value for unseen categories
default_encoded_value = 5


class AnimPrediction(APIView):
    def post(self, request, format=None):
        # Ensure XGBoost model is an instance of XGBRegressor
        if not isinstance(model2, XGBRegressor):
            return Response({"error": "Invalid data"}, status=400)

        # Extract input parameters from the request
        breed = request.data["breed"]
        health_status = request.data["health_status"]
        lactation_stage = request.data["lactation_stage"]
        reproductive_status = request.data["reproductive_status"]
        milking_frequency = request.data["milking_frequency"]
        age = float(request.data["age"])  # Ensure numeric data type
        nutrition_protein = float(
            request.data["nutrition_protein"]
        )  # Ensure numeric data type
        nutrition_carbohydrates = float(
            request.data["nutrition_carbohydrates"]
        )  # Ensure numeric data type
        nutrition_minerals = float(
            request.data["nutrition_minerals"]
        )  # Ensure numeric data type
        temperature = float(request.data["temperature"])  # Ensure numeric data type
        humidity = float(request.data["humidity"])  # Ensure numeric data type
        prev_milk_production = float(
            request.data["prev_milk_production"]
        )  # Ensure numeric data type

        try:
            breed_encoded = le.transform([breed])[0]
        except ValueError:
            # Handle unseen category, for example, assign a default value
            breed_encoded = default_encoded_value

        milking_frequency_encoded = le.transform([milking_frequency])[0]

        health_status_encoded = le.transform([health_status])[0]
        lactation_stage_encoded = le.transform([lactation_stage])[0]
        reproductive_status_encoded = le.transform([reproductive_status])[0]

        lis2 = [
            breed_encoded,
            health_status_encoded,
            lactation_stage_encoded,
            reproductive_status_encoded,
            milking_frequency_encoded,
            age,
            nutrition_protein,
            nutrition_carbohydrates,
            nutrition_minerals,
            temperature,
            humidity,
            prev_milk_production,
        ]

        # Print lis2 for debugging purposes
        print("Debug: lis2 =", lis2)

        # Ensure lis2 is a 2D array before making predictions
        lis2_reshaped = np.array(lis2).reshape(1, -1)

        # Predict using the model2
        predicted_milk_production = model2.predict(lis2_reshaped)

        # Return the prediction result in the response
        return Response(
            {"The expected milk production is": predicted_milk_production[0]},
            status=200,
        )
