import json
import os

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
    sample = pd.DataFrame(encode_values(sample))
    sample = add_calculated_columns(sample)

    return model.predict(sample)[0][0]

def encode_values(sample: pd.DataFrame) -> pd.DataFrame:
    sample.loc[0, "Société de taxis"] = 1 if sample.loc[0, "Société de taxis"] == "Creative Mobile Technologies, LLC" else 2
    sample.loc[0, "Type de paiement"] = 1 if sample.loc[0, "Société de taxis"] == "Carte de crédit" else 2
    
    return sample

def add_calculated_columns(sample: pd.DataFrame) -> pd.DataFrame:
    sample.loc[0, "day"] = sample.loc[0, "date"].day
    sample.loc[0, "hour"] = sample.loc[0, "time"].hour
    sample.loc[0, "is_night_trip"] = 1 if sample.loc[0, "hour"] < 5 else 0
    sample.loc[0, "airport_trip"] = 1 if "Airport" in sample.loc[0, "Lieu de départ"] \
                                    or "Airport" in sample.loc[0, "Lieu d'arrivée"] else 0
    sample.loc[0, "is_sunday"] = 1 if sample.loc[0, "day"] == 6 else 0

    sample.rename(columns={"Société de taxis": "VendorID", 
                            "Type de paiement": "payment_type", 
                            "Lieu de départ": "PULocationLabel", 
                            "Lieu d'arrivée": "DOLocationLabel"}, inplace=True)

    sample["day"] = sample["day"].astype(int)
    sample["hour"] = sample["hour"].astype(int)
    sample["is_night_trip"] = sample["is_night_trip"].astype(int)
    sample["airport_trip"] = sample["airport_trip"].astype(int)
    sample["is_sunday"] = sample["is_sunday"].astype(int)

    sample = sample[["VendorID", "passenger_count",
       "PULocationLabel", "DOLocationLabel", "payment_type", "day", "hour",
       "is_night_trip", "airport_trip", "is_sunday", "trip_distance"]]
    
    return sample