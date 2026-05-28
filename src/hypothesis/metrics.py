import numpy as np
import pandas as pd

def claim_frequency(df):
    """
    Proportion of policies with at least one claim
    """
    return (df["TotalClaims"] > 0).mean()


def claim_severity(df):
    """
    Average claim amount given a claim occurred
    """
    claims = df[df["TotalClaims"] > 0]["TotalClaims"]
    return claims.mean()


def margin(df):
    """
    Profitability metric
    """
    return df["TotalPremium"] - df["TotalClaims"]