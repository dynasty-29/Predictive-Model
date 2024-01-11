from django.apps import AppConfig
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

class FarmproducepredictionappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "FarmproducepredictionApp"
    model_path = "ML_models/plant_xgb_model"

    # Load the model with use_label_encoder set to False
    model = pickle.load(open(model_path, "rb"))
    model.use_label_encoder = True # Add this line

    label_encoder = LabelEncoder()


