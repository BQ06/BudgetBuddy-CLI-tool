import datetime
from dataclasses import dataclass
from typing import Optional, Literal
from __future__ import annotations

TxnType = Literal['income', 'expense', 'transfer']

@dataclass
class Transaction:
    id: int
    type: TxnType
    amount_pennies: int
    category: str
    date: datetime.date
    note: Optional[str] = None
    created_at: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)

@dataclass
class Budget:
    category: str
    monthly_limit_pennies: int

