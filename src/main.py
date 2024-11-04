# src/main.py
from config.config import *
from market_data import get_market_data, calculate_rsi
from sentiment_analysis import fetch_social_data, analyze_advanced_sentiment
from trading_strategy import calculate_signal
from order_execution import place_order
import time

def main():
    usd_balance = INVESTMENT
    crypto_balance = 0
    while True:
        try:
            # Récupérer les données de marché et calculer le RSI
            df = get_market_data()
            rsi = calculate_rsi(df, RSI_PERIOD)

            # Analyse de sentiment
            tweets = fetch_social_data(PAIR)
            sentiment = analyze_advanced_sentiment(tweets)

            # Calculer le signal de trading
            signal = calculate_signal(rsi, sentiment, OVERBOUGHT_THRESHOLD, OVERSOLD_THRESHOLD)

            # Exécuter les ordres en fonction du signal
            if signal == 'buy' and usd_balance > 0:
                amount_to_buy = usd_balance / df['close'].iloc[-1]
                place_order('buy', amount_to_buy)
                crypto_balance += amount_to_buy
                usd_balance = 0

            elif signal == 'sell' and crypto_balance > 0:
                usd_balance += crypto_balance * df['close'].iloc[-1]
                place_order('sell', crypto_balance)
                crypto_balance = 0

            # Pause avant la prochaine évaluation
            time.sleep(60)

        except Exception as e:
            print("Erreur:", e)
            time.sleep(60)

if __name__ == "__main__":
    main()
