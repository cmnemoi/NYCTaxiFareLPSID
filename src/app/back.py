import json
import os

import joblib
import pandas as pd

def load_form_fields() -> dict:
    try:
        with open("src/app/variables_labels.json") as f:
            return json.load(f)
    except FileNotFoundError as e:
        print(e)
        print(os.getcwd())

def get_trip_fare(data: dict) -> float:
    model = joblib.load("models/linear_regression_model.joblib")

    sample = pd.DataFrame.from_dict(data)
    sample = add_calculated_columns(sample)

    return model.predict(sample)[0][0]

def add_calculated_columns(sample: pd.DataFrame) -> pd.DataFrame:
    sample.loc[0, "day"] = sample.loc[0, "date"].day
    sample.loc[0, "hour"] = sample.loc[0, "time"].hour
    sample.loc[0, "is_night_trip"] = 1 if sample.loc[0, "hour"] < 5 else 0
    sample.loc[0, "airport_trip"] = 1 if "Airport" in sample.loc[0, "Lieu de départ"] or "Airport" in sample.loc[0, "Lieu d'arrivée"] else 0

    sample.rename(columns={"Société de taxis": "VendorID", 
                            "Type de paiement": "payment_type", 
                            "Lieu de départ": "PULocationLabel", 
                            "Lieu d'arrivée": "DOLocationLabel"}, inplace=True)

    sample["day"] = sample["day"].astype(int)
    sample["hour"] = sample["hour"].astype(int)
    sample["is_night_trip"] = sample["is_night_trip"].astype(int)
    sample["airport_trip"] = sample["airport_trip"].astype(int)
    
    return sample.drop(["date", "time"], axis=1)