import json

import joblib
import pandas as pd
import numpy as np

def trim(column: pd.Series) -> np.array:
    """Return a pandas.Series in which each value above 99e centile is trimmed at 99e centile"""
    quantile = column.quantile(q=.99)[0]
    return np.array([quantile if x[0] > quantile else x for x in column.values], dtype="object").reshape(-1, 1)

def load_form_fields() -> dict:
    with open("src/app/variables_labels.json") as f:
        return json.load(f)

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