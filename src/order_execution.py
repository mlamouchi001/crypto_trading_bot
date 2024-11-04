# src/order_execution.py
from config.config import TRANSACTION_FEE

def place_order(order_type, amount):
    amount_after_fee = amount * (1 - TRANSACTION_FEE)
    if order_type == 'buy':
        print(f"Achat simulé de {amount_after_fee} unités")
    elif order_type == 'sell':
        print(f"Vente simulée de {amount_after_fee} unités")
