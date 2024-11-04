# config/config.py

# Configuration de l'API de trading
API_KEY = "lZpO7N3imurDzkSLE0OG7czCKlrN8FlX15pkJkWaRaOFa4c4MABwa69UmQeksfSN"
SECRET_KEY = "9T5Zes1BfNBQp6Pruari6N4vNMvtPVcXdWVw1aZmDTLlk0FEHMsRo4r2stYL0ZYN"

# Configuration de l'API Twitter
TWITTER_API_KEY = "4QTjD4vJkAYoGmqNbfvucgdrp"
TWITTER_API_SECRET = "nU7VD7AZVSaeZ2EQw3GfYzaMYm9uvAxOg9LEqoEHAiUgZY2zYw"
TWITTER_ACCESS_TOKEN = "792057852336668672-eGs0PzExih0ZbK5N8DVwx9SCEoY5dfc"
TWITTER_ACCESS_TOKEN_SECRET = "AAAAAAAAAAAAAAAAAAAAAH%2FKwQEAAAAAKZIbKU9teqAdaxMYtJ40VyOBdtU%3D9Rko4gZMQkhB9Sm5ZI7Re7lNqwmw3sI88o1TkXUUA7rsPgwKhu"

# Paramètres de trading
PAIR = "BTC/USDT"             # Paire de trading par défaut (modifiable pour n'importe quelle crypto)
INVESTMENT = 100              # Montant en USDT pour chaque trade
RSI_PERIOD = 14               # Période de calcul du RSI
OVERBOUGHT_THRESHOLD = 70     # Seuil de surachat pour le RSI
OVERSOLD_THRESHOLD = 30       # Seuil de survente pour le RSI
TRANSACTION_FEE = 0.001       # Frais de transaction en pourcentage (0.1%)
TIMEFRAME = "1m"              # Intervalle de temps pour les bougies (modifiable, par exemple, "5m", "15m")
