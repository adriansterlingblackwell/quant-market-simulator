import pandas as pd
from strategy import generate_signal

def test_signal_column_created():

    df = pd.DataFrame({
        "close":[100,101],
        "sma_10":[99,100],
        "ema_20":[101,102],
        "rsi_20":[50,60],
        "vwap":[100,100]
    })

    result = generate_signal(df)

    assert "signal" in result.columns