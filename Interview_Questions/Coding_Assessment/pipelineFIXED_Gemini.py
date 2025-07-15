# This code is submission by Justin Bucsa for Eqvilent Code Assessment fpr the HFT Quantitative Researcher/ Trader role
# Contact Information:
# Name: Justin Bucsa
# E-Mail: Justin.Bucsa@gmail.com

import warnings

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

warnings.simplefilter(action="ignore", category=pd.errors.PerformanceWarning)


def print_price_std(df):
    # Calculate the standard deviation of the difference between 'high' and 'low'
    price_std = np.std(df["high"] - df["low"])
    print(price_std)


def prepare_data():
    df = pd.read_csv("Python-Library/Interview_Questions/Coding_Assessment/amgn.csv")
    base_cols = ["open", "high", "low", "close", "volume"]

    # Use forward fill for NaN values in OHLCV columns, then convert to float32
    df[base_cols] = df[base_cols].ffill().astype(np.float32)

    # Use a smaller shift for the target variable
    df["y"] = df["close"].shift(1).fillna(method="bfill")

    df["date"] = pd.to_datetime(df["date"])

    # Extract year, month, and day as separate features
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day

    base_cols = [c for c in df.columns if c not in ["y", "date"]]
    print(df)
    print(df.shape)
    print_price_std(df)
    return df[base_cols].copy(), df["y"]


def get_features(df):
    for name in df.columns:
        for period in [1, 9, 13, 117]:
            # Calculate the difference between current and shifted values, avoiding division by zero
            df[f"{name}_diff_{period}"] = df[name] - df[name].shift(period)

            df[f"{name}_median"] = df[name].rolling(period).median()
            df[f"{name}_std"] = df[name].rolling(period).std()
            df[f"{name}_max"] = df[name].rolling(period).max()
            df[f"{name}_min"] = df[name].rolling(period).min()
            df[f"{name}_quantile9"] = df[name].rolling(period).quantile(0.9)
            df[f"{name}_quantile99"] = df[name].rolling(period).quantile(0.99)
            df[f"{name}_rank"] = df[name].rank()

        for year in df["year"].unique():
            df.loc[df["year"] == year, f"{name}_relative_by_year"] = df[name] - df.loc[df["year"] == year, name].mean()

    # Use StandardScaler for feature scaling
    scaler = StandardScaler()
    for name in df.columns:
        df[name] = scaler.fit_transform(df[name].values.reshape(-1, 1))

    df["no_trades"] = (df["high"] == df["low"]).astype(int)
    return df


def main():
    X, y = prepare_data()
    X = get_features(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3, shuffle=False)

    params = {
        "objective": "regression",
        "metric": "rmse",
        "learning_rate": 0.1,
        "max_bin": 256,
        "min_data": 2000,
        "feature_fraction": 0.8,
        "verbose": -1,
    }
    train_data = lgb.Dataset(X_train, y_train)
    model = lgb.train(params, train_data, num_boost_round=1000)
    pred_val = model.predict(X_test)
    score = np.sqrt(mean_squared_error(y_test, pred_val))
    print(score)

    fe = pd.DataFrame()
    fe["feature"] = X_train.columns
    fe["importance"] = model.feature_importance(importance_type="split")
    fe = fe.sort_values("importance").reset_index(drop=True)
    print(fe.head(10))

    pred_test = model.predict(X_test)
    pd.Series(pred_test).to_csv("Python-Library/Interview_Questions/Coding_Assessment/pred_to_prod_Gemini.csv", index=False)


if __name__ == "__main__":
    main()