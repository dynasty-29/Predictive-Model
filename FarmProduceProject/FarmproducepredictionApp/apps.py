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
    def ready(self):
        # Path to the machine learning model file
        model_file_path = os.path.join(settings.BASE_DIR, 'ML_models', 'plant_xgb_model.pkl')

        # Load the machine learning model when the app is ready
        self.model = joblib.load(model_file_path)
    #
