import yfinance as yf
import pandas as pd

def load_data(stock_name, timeframe, interval):
    df = yf.download(
        tickers=stock_name,
        period=timeframe,
        interval=interval,
        auto_adjust=False,
        multi_level_index=False
    )

    if df.empty:
        raise ValueError(f"No data could be retrieved: {stock_name}")

    df = df.copy()
    df.reset_index(inplace=True)

    # Kolon isimlerini string'e çevir ve küçült
    df.columns = [str(col).strip().lower() for col in df.columns]

    required_cols = ["open", "high", "low", "close", "volume"]
    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    if df[required_cols].isna().all().all():
        raise ValueError(
            f"All OHLCV values are NaN for {stock_name} with period={timeframe}, interval={interval}"
        )

    return df