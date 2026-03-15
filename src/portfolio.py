def calculate_portfolio_value(cash, position, current_price):

    holdings_value = position * current_price
    equity = cash + holdings_value

    return holdings_value, equity