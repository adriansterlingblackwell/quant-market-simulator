import pandas as pd
import sys
sys.path.append(r"C:\Users\adria\OneDrive\Desktop\quant-market-simulator\config")
import config
import data_loader as data
import indicator as ind
import strategy as st
import simulation as sim
import metrics as met
import plot as pl


def get_input(prompt, default=None):
    value = input(prompt).strip()
    if value:
        return value
    if default is not None:
        return default
    raise ValueError(f"{prompt} cannot be empty!")


def print_data_summary(df, selected_column):
    print("\n--- DATA + INDICATORS + SIGNAL ---")
    print(df.columns.tolist())
    print(
        df[
            [
                selected_column,
                f"sma_{config.SMA_PERIOD}",
                f"ema_{config.EMA_PERIOD}",
                f"rsi_{config.RSI_PERIOD}",
                "vwap",
                "signal",
            ]
        ].tail(config.DISPLAY_ROWS)
    )


def print_simulation_summary(sim_df):
    print("\n--- SIMULATION RESULT ---")
    print(sim_df.columns.tolist())
    print(
        sim_df[
            [
                "close",
                "signal",
                "action",
                "cash",
                "position",
                "holdings_value",
                "equity",
            ]
        ].tail(config.DISPLAY_ROWS)
    )

    print("\n--- SIMULATION SUMMARY ---")
    print("Total rows:", len(sim_df))
    print("BUY_EXECUTED:", (sim_df["action"] == "BUY_EXECUTED").sum())
    print("SELL_EXECUTED:", (sim_df["action"] == "SELL_EXECUTED").sum())
    print("Final cash:", sim_df["cash"].iloc[-1])
    print("Final position:", sim_df["position"].iloc[-1])
    print("Final equity:", sim_df["equity"].iloc[-1])


def print_metrics(metrics_result):
    print("\n--- METRICS ---")
    print("Final equity:", metrics_result["final_equity"])
    print("Total return:", round(metrics_result["total_return"] * 100, 2), "%")
    print("Max drawdown:", metrics_result["max_drawdown"])
    print("Trade count:", metrics_result["trade_count"])


def main():
    df = pd.DataFrame()
    sim_df = pd.DataFrame()

    try:
        ticker_name = get_input(f"Stock name [{config.DEFAULT_TICKER}]: ", config.DEFAULT_TICKER).upper()
        ticker_timeframe = get_input(f"Timeframe [{config.DEFAULT_PERIOD}]: ", config.DEFAULT_PERIOD).lower()
        ticker_interval = get_input(f"Interval [{config.DEFAULT_INTERVAL}]: ", config.DEFAULT_INTERVAL).lower()
        selected_column = get_input(
            f"Which data [{config.DEFAULT_PRICE_COLUMN}]: ",
            config.DEFAULT_PRICE_COLUMN
        ).lower()

        df = data.load_data(ticker_name, ticker_timeframe, ticker_interval)

        df = ind.calculate_sma_ema(
            df,
            column=selected_column,
            sma_period=config.SMA_PERIOD,
            ema_period=config.EMA_PERIOD
        )
        df = ind.calculate_rsi(
            df,
            column=selected_column,
            period=config.RSI_PERIOD
        )
        df = ind.calculate_vwap(df)

        df = st.generate_signal(df)

        sim_df = sim.run_simulation(
            df,
            initial_cash=config.INITIAL_CASH,
            quantity=config.TRADE_QUANTITY
        )

        if not df.empty:
            print_data_summary(df, selected_column)

        if not sim_df.empty:
            print_simulation_summary(sim_df)

            metrics_result = met.calculate_metrics(
                sim_df,
                initial_cash=config.INITIAL_CASH
            )
            print_metrics(metrics_result)

            pl.plot_equity(sim_df)
            pl.plot_signals(sim_df)

           


    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
