import pandas as pd


def execute_trade(signal, price, cash, position, quantity=1):
    """
    Signal'e göre işlem uygular.
    BUY -> cash yeterliyse alım
    SELL -> position varsa satış
    """

    action = "HOLD"

    if signal == "BUY" and cash >= price * quantity:
        cash -= price * quantity
        position += quantity
        action = "BUY_EXECUTED"

    elif signal == "SELL" and position >= quantity:
        cash += price * quantity
        position -= quantity
        action = "SELL_EXECUTED"

    return cash, position, action


def calculate_portfolio_value(cash, position, current_price):
    """
    Portföy değerini hesaplar.
    """
    holdings_value = position * current_price
    equity = cash + holdings_value
    return holdings_value, equity


def run_simulation(df, initial_cash=10000, quantity=1):
    """
    Strategy tarafından üretilen signal kolonuna göre simülasyon çalıştırır.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    required_cols = ["close", "signal"]
    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    df = df.copy()

    cash = float(initial_cash)
    position = 0
    logs = []

    for _, row in df.iterrows():
        price = row["close"]
        signal = row["signal"]

        # timestamp varsa kullan, yoksa None bırak
        timestamp = row["timestamp"] if "timestamp" in df.columns else None

        if pd.isna(price):
            continue

        cash, position, action = execute_trade(
            signal=signal,
            price=price,
            cash=cash,
            position=position,
            quantity=quantity
        )

        holdings_value, equity = calculate_portfolio_value(
            cash=cash,
            position=position,
            current_price=price
        )

        logs.append({
            "timestamp": timestamp,
            "close": price,
            "signal": signal,
            "action": action,
            "cash": cash,
            "position": position,
            "holdings_value": holdings_value,
            "equity": equity
        })

    result_df = pd.DataFrame(logs)
    return result_df