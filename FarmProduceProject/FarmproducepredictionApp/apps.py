import os
import joblib
from django.apps import AppConfig
from django.conf import settings
import os
import pickle
from django.apps import AppConfig
from django.conf import settings


class FarmproducepredictionappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "FarmproducepredictionApp"
    model_path = "ML_models/plant_xgb_model.pkl"
    with open(model_path, "rb") as file:
        model = pickle.load(file)

    #


