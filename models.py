import datetime


class Transaction:
    id: int
    type: str
    amount: float
    category: str
    date: str
    note: str | None 
    created_at: datetime.datetime

class Budget:
    category: str
    monthly_limit: int

