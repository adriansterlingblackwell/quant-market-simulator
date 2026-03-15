import pandas as pd

def generate_signal(df):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    required_cols = ["close", "sma_10", "ema_20", "rsi_20", "vwap"]
    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    df = df.copy()
    signals = []

    for _, row in df.iterrows():
        if (
            pd.isna(row["sma_10"]) or
            pd.isna(row["ema_20"]) or
            pd.isna(row["rsi_20"]) or
            pd.isna(row["vwap"])
        ):
            signals.append("HOLD")
            continue

        if row["ema_20"] > row["sma_10"] and row["rsi_20"] < 70 and row["close"] > row["vwap"]:
            signals.append("BUY")
        elif row["ema_20"] < row["sma_10"] and row["rsi_20"] > 30 and row["close"] < row["vwap"]:
            signals.append("SELL")
        else:
            signals.append("HOLD")

    df["signal"] = signals
    return df