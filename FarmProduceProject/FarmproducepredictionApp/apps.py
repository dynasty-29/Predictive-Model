from django.apps import AppConfig
from xgboost import XGBClassifier, XGBRegressor
from sklearn.preprocessing import LabelEncoder
import pickle


class FarmproducepredictionappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "FarmproducepredictionApp"
    model_path1 = "ml_models/plant_xgb_model"
    model_path2 = "ml_models/animal_model"

    # Load the plant model
    model1 = pickle.load(open(model_path1, "rb"))
    model1.use_label_encoder = False  # Add this line

    # Load the animal model
    model2 = pickle.load(open(model_path2, "rb"))
    model2.use_label_encoder = False  # Add this line

    label_encoder = LabelEncoder()
