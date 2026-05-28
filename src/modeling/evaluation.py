import numpy as np
from sklearn.metrics import mean_squared_error, r2_score


def evaluate_model(model, X_test, y_test):
    pred = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, pred))
    r2 = r2_score(y_test, pred)

    return rmse, r2


def compare_models(results_dict):
    import pandas as pd

    return pd.DataFrame(results_dict)