from django.apps import AppConfig
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
import pickle


class FarmproducepredictionappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "FarmproducepredictionApp"
    model_path = "ML_models/plant_xgb_model.pkl"

    # Load the model without setting use_label_encoder
    model = pickle.load(open(model_path, "rb"))

    label_encoder = LabelEncoder()
