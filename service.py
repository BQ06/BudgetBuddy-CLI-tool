import os
import json
from models import Transaction, Budget
# add transactions from JSON file
def add_transaction(transaction: Transaction):
    """Add a new transaction to the storage."""
    transactions = load_transactions()
    transactions.append(transaction.__dict__)
    save_transactions(transactions)
    
#  list transactions from JSON file

def list_transactions():
    """List all transactions from the storage."""
    return load_transactions()

# delete transaction by ID from JSON file 
def delete_transaction(transaction_id: int):
    """Delete a transaction by its ID."""
    transactions = load_transactions()
    transactions = [t for t in transactions if t['id'] != transaction_id]
    save_transactions(transactions)

# summarize transactions by all date ranges
def summarise(transactions, date_from=None, date_to=None):
    """Summarise transactions within a date range."""
    filtered = []
    for t in transactions:
        t_date = datetime.datetime.strptime(t['date'], '%Y-%m-%d').date()
        if (date_from is None or t_date >= date_from) and (date_to is None or t_date <= date_to):
            filtered.append(t)
    total_income = sum(t['amount'] for t in filtered if t['type'] == 'income')
    total_expense = sum(t['amount'] for t in filtered if t['type'] == 'expense')
    return {
        'total_income': total_income,
        'total_expense': total_expense,
        'net_savings': total_income - total_expense
    }
