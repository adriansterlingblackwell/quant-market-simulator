import pandas as pd

def calculate_metrics(sim_df, initial_cash):

    equity = sim_df["equity"]

    final_equity = equity.iloc[-1]

    total_return = (final_equity - initial_cash) / initial_cash

    running_max = equity.cummax()
    drawdown = equity - running_max
    max_drawdown = drawdown.min()

    trade_count = (sim_df["action"] != "HOLD").sum()
    
    return {
        "final_equity": final_equity,
        "total_return": total_return,
        "max_drawdown": max_drawdown,
        "trade_count": trade_count
    }