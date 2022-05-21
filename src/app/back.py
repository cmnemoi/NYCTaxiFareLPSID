import joblib
import json

def load_form_fields() -> dict:
    with open("variables_labels.json") as f:
        return json.load(f)

def get_trip_fare() -> float:
    model = load("models/linear_regression_model.joblib")