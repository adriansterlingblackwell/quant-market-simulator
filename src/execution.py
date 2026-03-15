def execute_trade(signal, price, cash, position, quantity=1):

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