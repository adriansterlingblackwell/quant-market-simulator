import matplotlib.pyplot as plt


def plot_equity(sim_df):
    if sim_df.empty:
        raise ValueError("sim_df is empty")

    if "equity" not in sim_df.columns:
        raise ValueError("equity column not found")

    plt.figure(figsize=(10, 5))
    plt.plot(sim_df["equity"], label="Equity Curve")
    

    plt.title("Equity Curve")
    plt.xlabel("Step")
    plt.ylabel("Equity")

    plt.legend()
    plt.grid(True)
    plt.show()


def plot_signals(sim_df):
    if sim_df.empty:
        raise ValueError("sim_df is empty")

    required_cols = ["close", "action"]
    missing_cols = [col for col in required_cols if col not in sim_df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    buys = sim_df[sim_df["action"] == "BUY_EXECUTED"]
    sells = sim_df[sim_df["action"] == "SELL_EXECUTED"]

    plt.figure(figsize=(12, 6))
    plt.plot(sim_df["close"], label="Close Price")

    plt.scatter(buys.index, buys["close"], marker="^", s=100, label="Buy")
    plt.scatter(sells.index, sells["close"], marker="v", s=100, label="Sell")

    plt.title("Trading Signals")
    plt.xlabel("Step")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()
