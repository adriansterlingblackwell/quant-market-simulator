import pandas as pd

def calculate_sma_ema(df_data, column, sma_period=20, ema_period=15):
    if not isinstance(df_data, pd.DataFrame):
        raise TypeError("df_data must be a pandas DataFrame")

    if column not in df_data.columns:
        raise ValueError(f"{column} column not found")

    if sma_period <= 0 or ema_period <= 0:
        raise ValueError("Periods must be positive")

    df_data = df_data.copy()

    df_data[f"sma_{sma_period}"] = df_data[column].rolling(window=sma_period).mean()
    df_data[f"ema_{ema_period}"] = df_data[column].ewm(span=ema_period, adjust=False).mean()

    return df_data


def calculate_rsi(df_data, column, period):
    if not isinstance(df_data, pd.DataFrame):
        raise TypeError("df_data must be a pandas DataFrame")

    if column not in df_data.columns:
        raise ValueError(f"{column} column not found")

    if period <= 0:
        raise ValueError("Period must be positive")

    df_data = df_data.copy()

    delta = df_data[column].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss.replace(0, pd.NA)
    rsi = 100 - (100 / (1 + rs))

    df_data[f"rsi_{period}"] = rsi

    return df_data


def calculate_vwap(df_data):
    if not isinstance(df_data, pd.DataFrame):
        raise TypeError("df_data must be a pandas DataFrame")

    required_cols = ["high", "low", "close", "volume"]
    for col in required_cols:
        if col not in df_data.columns:
            raise ValueError(f"{col} column not found, VWAP cannot be calculated")

    df_data = df_data.copy()

    tp = (df_data["high"] + df_data["low"] + df_data["close"]) / 3
    cum_vol_price = (tp * df_data["volume"]).cumsum()
    cum_vol = df_data["volume"].cumsum()

    df_data["vwap"] = cum_vol_price / cum_vol

    return df_data