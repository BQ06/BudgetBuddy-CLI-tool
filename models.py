import datetime
from dataclasses import dataclass
from typing import Optional, Literal
import __future__

TxnType = Literal['income', 'expense', 'transfer']

@dataclass
class Transaction:
    id: int
    type: TxnType
    amount_pennies: int
    category: str
    date: datetime.date
    note: Optional[str]
    created_at: datetime

class Budget:
    category: str
    monthly_limit: int

