import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import numpy as np


@api_view(['GET'])
def index_page(request):
    return_data = {
        "error" : "0",
        "message" : "Successful",
    }
    return Response(return_data)


@api_view(["POST"])
def predict_croptype(request):
    try:
        temperature = request.GET['temperature']
        humidity = request.GET['humidity']
        precipitation = request.GET['precipitation']
        wind_speed = request.GET['wind_speed']
        solar_radiation = request.GET['solar_radiation']
        nitrogen_level = request.GET['nitrogen_level']
        phosphorus_level = request.GET['phosphorus_level']
        potassium_level = request.GET['potassium_level']
        ph_level = request.GET['ph_level']
        fields = [temperature, humidity, precipitation, wind_speed, solar_radiation,
                  nitrogen_level, phosphorus_level, potassium_level, ph_level]
        if not None in fields:
            temperature=temperature,
            humidity=humidity,
            precipitation=precipitation,
            wind_speed=wind_speed,
            solar_radiation=solar_radiation,
            nitrogen_level=nitrogen_level,
            phosphorus_level=phosphorus_level,
            potassium_level=potassium_level,
            ph_level=ph_level,
            result = [temperature, humidity, precipitation, wind_speed, solar_radiation,
                  nitrogen_level, phosphorus_level, potassium_level, ph_level]
            model_path = 'Ml_model/plant_xgb_model.pkl'
            classifier = pickle.load(open(model_path, 'rb'))
            prediction = classifier.predict([result])[0]
            conf_score = np.max(classifier.predict_proba([result])) * 100
            predictions = {
                'error': '0',
                'message': 'Successfull',
                'prediction': prediction,
                'confidence_score': conf_score
            }

        else:
            predictions = {
                'error': '1',
                'message': 'Invalid Parameters'
            }

    except Exception as e:
        predictions = {
            'error': '2',
            "message": str(e)
        }

    return Response(predictions)
