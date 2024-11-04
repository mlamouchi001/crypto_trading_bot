# src/market_data.py
import ccxt
import pandas as pd
from config.config import API_KEY, SECRET_KEY, PAIR, TIMEFRAME, RSI_PERIOD

# Initialiser l'API de Binance
exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': SECRET_KEY,
    'enableRateLimit': True,
})

def get_market_data():
    """
    Récupère les données OHLCV pour la paire configurée.

    Returns:
        pd.DataFrame: Un DataFrame contenant les données OHLCV.
    """
    ohlcv = exchange.fetch_ohlcv(PAIR, timeframe=TIMEFRAME, limit=RSI_PERIOD + 1)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def calculate_rsi(df, period):
    """
    Calcule le RSI pour une période donnée.

    Parameters:
        df (pd.DataFrame): Le DataFrame contenant les prix de clôture.
        period (int): La période de calcul du RSI.

    Returns:
        float: Le RSI calculé.
    """
    delta = df['close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1]
