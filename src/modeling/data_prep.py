import pandas as pd
import numpy as np


def load_data(path):
    df = pd.read_csv(path, sep="|")
    return df


def clean_data(df):
    df = df.copy()

    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    df = df.dropna(subset=["TotalClaims", "TotalPremium"])

    return df


def create_severity_dataset(df):
    df = df[df["TotalClaims"] > 0].copy()
    return df