# Quant Market Simulator

A modular Python-based market simulation project designed to explore the core workflow of quantitative trading research.

This project demonstrates a simplified research pipeline used in quantitative finance, including data collection, indicator generation, strategy signals, trade execution, portfolio tracking, performance metrics, and visualization.

The goal of this project is educational: to understand how a basic quantitative trading system is structured and how each component interacts.

---

## Project Architecture

The system follows a modular pipeline structure:

Data → Indicators → Strategy → Execution → Portfolio → Simulation → Metrics → Visualization

Each step is separated into individual modules to keep the system readable, extendable, and testable.

---

## Project Structure

```
quant-market-simulator/

config.py
main.py

data_loader.py
indicator.py
strategy.py

execution.py
portfolio.py
simulation.py

metrics.py
plot.py

tests/
    test_strategy.py
    test_portfolio.py

README.md
requirements.txt
```

---

## Module Overview

### data_loader.py

Handles market data retrieval using yfinance and performs basic data validation and cleaning.

Responsibilities:

* Download OHLCV market data
* Normalize column names
* Validate required columns

---

### indicator.py

Calculates technical indicators used by the strategy.

Current indicators:

* Simple Moving Average (SMA)
* Exponential Moving Average (EMA)
* Relative Strength Index (RSI)
* Volume Weighted Average Price (VWAP)

---

### strategy.py

Generates trading signals based on indicator values.

Signal outputs:

* BUY
* SELL
* HOLD

Example logic:

* EMA crossover
* RSI thresholds
* VWAP trend confirmation

---

### execution.py

Executes trades based on strategy signals.

Responsibilities:

* Validate buy/sell conditions
* Update cash and position

---

### portfolio.py

Tracks portfolio value over time.

Calculates:

* holdings value
* total equity

---

### simulation.py

Runs the market simulation engine.

Responsibilities:

* Iterate over market data
* Apply signals
* Execute trades
* Record portfolio history

---

### metrics.py

Evaluates trading performance.

Metrics include:

* Final equity
* Total return
* Maximum drawdown
* Trade count

---

### plot.py

Visualizes simulation results.

Current charts:

* Equity curve
* Price with trade markers (optional)

---

### config.py

Central configuration file for project parameters.

Examples:

* indicator periods
* trading quantity
* initial capital
* default market settings

---

## Running the Project

Install dependencies:

```
pip install -r requirements.txt
```

Run the simulator:

```
python main.py
```

You will be prompted for:

* Stock ticker
* Timeframe
* Data interval
* Price column

The system will then:

1. Download market data
2. Calculate indicators
3. Generate signals
4. Run trading simulation
5. Display performance results

---

## Example Output

The simulation prints:

* Data with indicators and signals
* Simulation trade log
* Final performance summary

Example metrics:

```
Final equity: 10523
Total return: 5.23%
Max drawdown: -2.1%
Trade count: 14
```

---

## Future Improvements

Planned upgrades include:

* commission & slippage modeling
* risk management rules
* multi-asset simulation
* Sharpe ratio & advanced metrics
* parameter optimization
* event-driven backtesting engine

---

## Educational Purpose

This project is intended as a learning framework for understanding:

* quantitative trading system architecture
* backtesting logic
* modular financial software design
* Python-based financial research workflows

---

## License

MIT License
