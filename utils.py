import datetime
from calendar import monthrange
from decimal import Decimal, ROUND_HALF_UP

# https://docs.python.org/3/library/datetime.html#aware-and-naive-objects used for date parsing understanding 

def parse_date(s: str):
    """Parse a date string in YYYY-MM-DD format."""
    return datetime.datetime.strptime(s, '%Y-%m-%d').date()

# datetime.datetime used to convert string to date object
def parse_month(s: str) -> tuple[datetime.date, datetime.date]:
    d = datetime.datetime.strptime(s, '%Y-%m').date()
    last_day = monthrange(d.year, d.month)[1]
    """Parse a month string in YYYY-MM format."""
    return datetime.date(d.year, d.month, 1), datetime.date(d.year, d.month, last_day)

def parse_amount(s: str):  # https://stackoverflow.com/questions/379906/how-do-i-parse-a-string-to-a-float-or-int
    """Parse a amount str to an int.  12.50 == 1250 pennies"""
    try:
        return int(round(float(s) * 100))
    except (ValueError, TypeError):
        return print("Please enter a Valid amount as a number")
                        

def format_money(pennies: int): # https://docs.python.org/3/library/decimal.html used for money formatting
    pounds = Decimal(pennies) / Decimal(100)
    return f"£{pounds:.2f}"

def validate_type(t: str):
    validate_types = {'income', 'expense', 'transfer'}
    if t not in validate_types:
        raise ValueError(f"Invalid type: {t}. Must be one of {validate_types}")
        return t

def date_in_range(d: datetime.date, start: datetime.date, end: datetime.date):
    if start <= d <= end: # function checks if the date d is between start and end
        return True
    else:
        return False
    