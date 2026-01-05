import json
import os.path
from models import Transaction, Budget

# Used this to help with logic for JSON handling  https://realpython.com/python-json/#writing-json-with-python

def load_data():
    """Load transactions and budgets from JSON files."""
    transactions = []
    budgets = []
    if os.path.exists('Transaction.json') == True:
        with open('Transaction.json') as f:
            transactions = json.load(f)
    else:
        pass
    if os.path.exists('Budget.json') == True:
        with open('Budget.json') as f:
            budgets = json.load(f)
    else:
        pass
    return transactions, budgets

# copied from above link, 'w' mode overwrites existing file or creates new one and f is the file object. 
def save_data(transactions, budgets):
    """Save transactions and budgets to JSON files."""
    with open('Transaction.json', 'w') as f:
        json.dump(transactions, f, indent=4)
    with open('Budget.json', 'w') as f:
        json.dump(budgets, f, indent=4)
    return transactions, budgets