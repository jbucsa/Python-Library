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
    _high[_high == _low] = np.nan  # Replacing equal values with NaN might skew the results
    _low[_high == _low] = np.nan # Replacing equal values with NaN might skew the results AND _low is currently retaining the same value as _high, resulting in a nanstd equal to 0 (ZERO) for all values. 
    # Solution would be to drop values when "high" and "low" both are not present. Before proceeding to the next step. Or wait till the prepare_data() step to remove all NaN values.
    print(np.nanstd(_high - _low)) # Currently nanstd is equal to 0 (ZERO) when _high AND _low are storing the same value. This may skew the results at unique or critical points. Print statement may be useful to help identify when NaN or 0 (ZERO) occurres. Data cleaning would still be needed. 


def prepare_data():
    df = pd.read_csv("amgn.csv")
    base_cols = ["open", "high", "low", "close", "volume"]
    df[base_cols] = df[base_cols].fillna(0).astype(np.float32)  # Filling NaN with 0 (ZERO) can distort the data. Use forward fill for NaN values in OHLCV columns, then convert to float32. 
    # Solution (1) would be writing the following: df[base_cols] = df[base_cols].ffill().astype(np.float32).
    # Solution (2) would be to drop values when NaN is present as it may skew the results at unique or critical points
    df["y"] = df["close"].shift(100).fillna(0)  # Large shift, might lose valuable data. Using .fillna(0) can introduce artificial values in y, which is incorrect for training a model. Use a smaller shift for the target variable. 
    # Solution (1)  would be writing the following: df["y"] = df["close"].shift(1).fillna(method="bfill")
    # Solution (2) would be to keep the same code but do not include the ".fillna(0) statement"

    df["date"] = pd.to_datetime(df["date"])
    df["year"], df["month"], df["day"] = df["date"].dt.year % 10, df["date"].dt.month, df["date"].dt.day  # Year % 10 might not be the best way to represent years. df["year"] = df["date"].dt.year % 10 reduces year values to a single digit (e.g., 2023 becomes 3), which causes an incorrect representation. Keeping the 2023 value may represent as key information in later analysis.
    # Solution (1)  would be the following for extract year, month, and day as separate features:
    # df["year"] = df["date"].dt.year
    # df["month"] = df["date"].dt.month
    # df["day"] = df["date"].dt.day
    # Solution (2)  would be the following for extract year, month, and day as separate features:
    # df["year"], df["month"], df["day"] = df["date"].dt.year, df["date"].dt.month, df["date"].dt.day

    base_cols = [c for c in df.columns if c not in ["y", "date"]]
    print(df)
    print(df.shape)
    print_price_std(df)
    return df[base_cols].copy(), df["y"]


def get_features(df):
    for n, name in enumerate(df.columns):
        for period in [1, 9, 13, 117]:
        
            df[f"{name}_diff_{period}"] = df[name].shift(period) / df[name]  # Division by 0 (ZERO) is possible. One method would be to calculate the difference between current and shifted values, avoiding division by zero
            # Solution would be writing the following: 
            # df[f"{name}_diff_{period}"] = df[name].shift(period) / df[name].replace(0, np.nan)
            # Note this Solution may create NaN values that would need to be dropped if created. NaN values may skew the data.
            df[f"{name}_median"] = df[name].rolling(period).median()
            df[f"{name}_std"] = df[name].rolling(period).std()
            df[f"{name}_max"] = df[name].rolling(period).max()
            df[f"{name}_min"] = df[name].rolling(period).min()
            df[f"{name}_quantile9"] = df[name].rolling(period).quantile(0.9)
            df[f"{name}_quantile99"] = df[name].rolling(period).quantile(0.99)
            df[f"{name}_rank"] = df[name].rank() #Ranking makes little sense without context or normalization.  
            # Solution would be to standardize ranks within a specific window.
            # df.loc[df["year"] == year, f"{name}_relative_by_year"] = df[name] - df.loc[df["year"] == year, name].mean()
            # Note this may create NaN values, switch may need to be dropped to prevent skewing of data.

        for year in df["year"].unique():
            df.loc[df["year"] == year, f"{name}_relative_by_year"] = df[name] - df.loc[df["year"] == year, name].mean() # df.loc[df["year"] == year, f"{name}_relative_by_year"] = df[name] - df.loc[df["year"] == year, name].mean()
            # Solution, in case NaN values do exist, you can use the following code but ideally, the data should be clean by this point.
            # df.loc[df["year"] == year, f"{name}_relative_by_year"] = df[name] - df.loc[df["year"] == year, name].mean()



    for name in df.columns:
        df[name] = (df[name] - df[name].min()) / (df[name].max() - df[name].min())  # MinMax scaling might not be the best choice. One method to solution is would be to use StandardScaler from sklearn.preprocessing for feature scaling.
    # Solution would be writing the following:
    # scaler = StandardScaler()
    # for name in df.columns:
    #   df[name] = scaler.fit_transform(df[name].values.reshape(-1, 1)) 

    df["no_trades"] = (df["high"] == df["low"]).astype(int)
    return df


def main():
    X, y = prepare_data()
    X = get_features(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3)
    X_train2, X_val, y_train2, y_val = train_test_split(X_train, y_train, train_size=0.7, test_size=0.3)  # Splitting the data twice might lead to data leakage. This is either a step that was accidentally copied twice or is purposely splitting the data twice. A discussion with the design engineer would be encouraged for a code review about this step. 

    params = {
        "loss": "mape",  # MAPE is not always the best metric for calculating loss. Suggestion of renaming to:
        # "metric": "mape"
        "learning_rate": 1,  # High learning rate can lead to overfitting. Suggestion of lowering the learning rate to values between 0.05 < x < 0.3. Testing to find ideal learning rate is suggested as well.
        "max_bin": 256,
        "min_data": 2000,
        "feature_fraction": 0.1,
        "verbose": -1,
    }
    train_data = lgb.Dataset(X_train2, y_train2)
    model = lgb.train(params, train_data, num_boost_round=1000)  # No early stopping
    pred_val = model.predict(X_val)
    score = mean_absolute_error(y_val, pred_val)
    print(score)

    fe = pd.DataFrame()
    fe["feature"] = X_train.columns
    fe["importance"] = model.feature_importance(importance_type="split") # feature_importance(importance_type="split") is not informative. "gain" is preferred. How the importance is calculated. If "split", result contains numbers of times the feature is used in a model. If "gain", result contains total gains of splits which use the feature. "gain" may be the more ideal value this model is searching for. A discussion with the design engineer would be encouraged for a code review about this step.
    # Solution to this code would be the following if "gain" is the desired outcome:
    # fe["importance"] = model.feature_importance(importance_type="gain")
    fe = fe.sort_values("importance").reset_index(drop=True)
    print(fe.head(10))

    pred_test = model.predict(X_test)
    pd.Series(pred_test).to_csv("pred_to_prod.csv", index=False) #Saving a prediction series without a corresponding index can be confusing.
    # Solution would be to add an index column to the CSV output.
    # Additionally, in case NaN values still exist at this point, the design could add the following code to get the CSV fill formatted. This code would start following Line 117 : pred_test = model.predict(X_test)
    # pred_test = pd.Series(pred_test).interpolate().fillna(method='bfill').fillna(method='ffill').values  # Replace NaNs with interpolated values
    # output_df = pd.DataFrame({"index": range(len(pred_test)), "prediction": pred_test})
    # output_df.to_csv("pred_to_prod.csv", index=False)  # Fixed CSV formatting


if __name__ == "__main__":
    main()