from portfolio import calculate_portfolio_value

def test_portfolio_value():

    holdings, equity = calculate_portfolio_value(
        cash=5000,
        position=2,
        current_price=100
    )

    assert holdings == 200
    assert equity == 5200