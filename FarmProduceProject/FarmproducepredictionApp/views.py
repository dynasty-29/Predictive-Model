import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import numpy as np

@api_view(["POST"])
def predict_croptype(request):
    try:
        required_params = ['temperature', 'humidity', 'precipitation', 'wind_speed', 'solar_radiation',
                           'nitrogen_level', 'phosphorus_level', 'potassium_level', 'ph_level']

        if all(param in request.data for param in required_params):
            result = [request.data[param] for param in required_params]

            model_path = 'ML_models/plant_xgb_model.pkl'
            classifier = pickle.load(open(model_path, 'rb'))
            prediction = classifier.predict([result])[0]
            conf_score = np.max(classifier.predict_proba([result])) * 100
            predictions = {
                'error': '0',
                'message': 'Successful',
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
