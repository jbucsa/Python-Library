# This code is submission by Justin Bucsa for Eqvilent Code Assessment fpr the HFT Quantitative Researcher/ Trader role
# Contact Information:
# Name: Justin Bucsa
# E-Mail: Justin.Bucsa@gmail.com

import warnings
import numpy as np
import pandas as pd
import lightgbm as lgb
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

warnings.simplefilter(action="ignore", category=pd.errors.PerformanceWarning)


def print_price_std(df):
    _high = df["high"].values
    _low = df["low"].values
    _high[_high == _low] = np.nan
    _low[_high == _low] = np.nan
    print(np.nanstd(_high - _low))


def prepare_data():
    df = pd.read_csv("amgn.csv")
    base_cols = ["open", "high", "low", "close", "volume"]
    df[base_cols] = df[base_cols].fillna(0).astype(np.float32)
    df["y"] = df["close"].shift(100).fillna(0)
    df["date"] = pd.to_datetime(df["date"])
    df["year"], df["month"], df["day"] = df["date"].dt.year % 10, df["date"].dt.month, df["date"].dt.day
    base_cols = [c for c in df.columns if c not in ["y", "date"]]
    print(df)
    print(df.shape)
    print_price_std(df)
    return df[base_cols].copy(), df["y"]


def get_features(df):
    for n, name in enumerate(df.columns):
        for period in [1, 9, 13, 117]:
            df[f"{name}_diff_{period}"] = df[name].shift(period) / df[name]
            df[f"{name}_median"] = df[name].rolling(period).median()
            df[f"{name}_std"] = df[name].rolling(period).std()
            df[f"{name}_max"] = df[name].rolling(period).max()
            df[f"{name}_min"] = df[name].rolling(period).min()
            df[f"{name}_quantile9"] = df[name].rolling(period).quantile(0.9)
            df[f"{name}_quantile99"] = df[name].rolling(period).quantile(0.99)
            df[f"{name}_rank"] = df[name].rank()

        for year in df["year"].unique():
            df.loc[df["year"] == year, f"{name}_relative_by_year"] = df[name] - df.loc[df["year"] == year, name].mean()

    for name in df.columns:
        df[name] = (df[name] - df[name].min()) / (df[name].max() - df[name].min())

    df["no_trades"] = (df["high"] == df["low"]).astype(int)
    return df


def main():
    X, y = prepare_data()
    X = get_features(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3)
    X_train2, X_val, y_train2, y_val = train_test_split(X_train, y_train, train_size=0.7, test_size=0.3)

    params = {
        "loss": "mape",
        "learning_rate": 1,
        "max_bin": 256,
        "min_data": 2000,
        "feature_fraction": 0.1,
        "verbose": -1,
    }
    train_data = lgb.Dataset(X_train2, y_train2)
    model = lgb.train(params, train_data, num_boost_round=1000)
    pred_val = model.predict(X_val)
    score = mean_absolute_error(y_val, pred_val)
    print(score)

    fe = pd.DataFrame()
    fe["feature"] = X_train.columns
    fe["importance"] = model.feature_importance(importance_type="split")
    fe = fe.sort_values("importance").reset_index(drop=True)
    print(fe.head(10))

    pred_test = model.predict(X_test)
    pd.Series(pred_test).to_csv("pred_to_prod.csv", index=False)


if __name__ == "__main__":
    main()
