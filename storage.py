from  __future__ import annotations
import json, os
from typing import Any, Dict, List, TypedDict

class StorageData(TypedDict):
    next_id: int
    transactions: List[Dict[str, Any]]

DEFAULT_DATA_DIR = os.path.join(os.path.expanduser("~"), ".budget_buddy")
DEFAULT_FILE = os.path.join(DEFAULT_DATA_DIR, "transactions.json")

def ensure_file(path: str = DEFAULT_FILE) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"next_id": 1, "transactions": []}, f, indent=2)

def load_data(path: str = DEFAULT_FILE) -> StorageData:
    ensure_file(path)
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict) or "next_id" not in data or "transactions" not in data:
            # fail-safe: reset to empty-but-valid
            return {"next_id": 1, "transactions": []}
        if not isinstance(data["transactions"], list):
            return {"next_id": int(data.get("next_id", 1)), "transactions": []}
        return {"next_id": int(data["next_id"]), "transactions": data["transactions"]}
    except json.JSONDecodeError:
        return {"next_id": 1, "transactions": []}

def save_data(data: StorageData, path: str = DEFAULT_FILE) -> None:
    ensure_file(path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
