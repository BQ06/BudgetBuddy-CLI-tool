from __future__ import annotations

import json
import os
from datetime import date, datetime
from typing import Any, Dict, List, Optional, Tuple

from models import Transaction  # Budget not needed in this file yet


# Pull in JSON from storage
DEFAULT_DATA_DIR = os.path.join(os.path.expanduser("~"), ".budget_buddy")
DEFAULT_FILE = os.path.join(DEFAULT_DATA_DIR, "Transaction.json")


def ensure_file(path: str = DEFAULT_FILE) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f)


def load_transactions(path: str = DEFAULT_TXN_FILE) -> List[Dict[str, Any]]:
    """Load transactions from disk as a list of dicts."""
    _ensure_data_file(path)
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("Transactions.json must contain a JSON array")
        return data
    except json.JSONDecodeError:
        # If file is corrupt/empty, fail safely to empty list
        return []


def save_transactions(transactions: List[Dict[str, Any]], path: str = DEFAULT_TXN_FILE) -> None:
    """Persist transactions to disk."""
    _ensure_data_file(path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(transactions, f, indent=2, ensure_ascii=False)


def _parse_date(value: Any) -> date:
    """
    Accepts:
      - date object
      - 'YYYY-MM-DD' string
    Returns a date object.
    """
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, str):
        return datetime.strptime(value, "%Y-%m-%d").date()
    raise ValueError(f"Invalid date value: {value!r} (expected date or 'YYYY-MM-DD')")


def _to_dict(txn: Transaction) -> Dict[str, Any]:
    """
    Convert a Transaction model to JSON-safe dict.
    Ensures date is saved as YYYY-MM-DD.
    """
    d = txn.__dict__.copy()
    if "date" in d:
        d["date"] = _parse_date(d["date"]).isoformat()
    return d


def _next_id(existing: List[Dict[str, Any]]) -> int:
    max_id = 0
    for t in existing:
        try:
            max_id = max(max_id, int(t.get("id", 0)))
        except (TypeError, ValueError):
            continue
    return max_id + 1


def add_transactions(
    new_txns: List[Transaction],
    path: str = DEFAULT_TXN_FILE,
    next_id: Optional[int] = None,
) -> Tuple[List[Dict[str, Any]], int]:
    """
    Add one or many new Transaction objects to storage.
    Assigns IDs automatically unless next_id provided.

    Returns:
      (updated_transactions_as_dicts, next_id_after_insert)
    """
    transactions = load_transactions(path)

    if next_id is None:
        next_id = _next_id(transactions)

    for txn in new_txns:
        txn.id = next_id
        transactions.append(_to_dict(txn))
        next_id += 1

    save_transactions(transactions, path)
    return transactions, next_id

#  list transactions from JSON file
def list_transactions(
    path: str = DEFAULT_TXN_FILE,
    txn_type: Optional[str] = None,
    category: Optional[str] = None,
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
) -> List[Dict[str, Any]]:
    """
    List transactions with optional filters.
    """
    txns = load_transactions(path)

    if txn_type:
        txns = [t for t in txns if t.get("type") == txn_type]

    if category:
        txns = [t for t in txns if t.get("category") == category]

    if date_from is not None:
        df = _parse_date(date_from)
        txns = [t for t in txns if _parse_date(t.get("date")) >= df]

    if date_to is not None:
        dt = _parse_date(date_to)
        txns = [t for t in txns if _parse_date(t.get("date")) <= dt]

    return txns


def delete_transaction(
    txn_id: int,
    path: str = DEFAULT_TXN_FILE
) -> List[Dict[str, Any]]:
    """
    Delete a transaction by ID. Returns updated list.
    """
    txns = load_transactions(path)
    updated = [t for t in txns if int(t.get("id", -1)) != txn_id]
    save_transactions(updated, path)
    return updated

# summarize transactions by all date ranges

def summarise(
    path: str = DEFAULT_TXN_FILE,
    date_from: Optional[date] = None,
    date_to: Optional[date] = None
) -> Dict[str, float]:
    """
    Summarise transactions in optional date range.
    Returns totals for income, expense, and net_savings.
    """
    txns = load_transactions(path)

    filtered: List[Dict[str, Any]] = []
    for t in txns:
        try:
            t_date = _parse_date(t.get("date"))
        except Exception:
            continue

        if date_from is not None and t_date < _parse_date(date_from):
            continue
        if date_to is not None and t_date > _parse_date(date_to):
            continue

        filtered.append(t)

    def _amount(x: Any) -> float:
        try:
            return float(x)
        except (TypeError, ValueError):
            return 0.0

    total_income = sum(_amount(t.get("amount")) for t in filtered if t.get("type") == "income")
    total_expense = sum(_amount(t.get("amount")) for t in filtered if t.get("type") == "expense")

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_savings": total_income - total_expense,
    }