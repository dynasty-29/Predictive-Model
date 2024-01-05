import os
import joblib
from django.apps import AppConfig
from django.conf import settings
import os
import joblib
from django.apps import AppConfig
from django.conf import settings
class FarmproducepredictionappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FarmproducepredictionApp'
    MODEL_File = os.path.join(settings.MODELS, "plant_xgb_model.pkl")
    model = joblib.load(MODEL_File)
    #
