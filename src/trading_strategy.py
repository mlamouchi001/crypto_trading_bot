# src/trading_strategy.py
def calculate_signal(rsi, sentiment, overbought_threshold, oversold_threshold):
    if rsi < oversold_threshold and sentiment > 0:
        return 'buy'
    elif rsi > overbought_threshold and sentiment < 0:
        return 'sell'
    return 'hold'
