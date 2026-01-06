import datetime
from calendar import monthrange
from decimal import Decimal, ROUND_HALF_UP

# https://docs.python.org/3/library/datetime.html#aware-and-naive-objects used for date parsing understanding 

def parse_date(s: str):
    """Parse a date string in YYYY-MM-DD format."""
    return datetime.datetime.strptime(s, '%Y-%m-%d').date()

# datetime.datetime used to convert string to date object
def parse_month(s: str):
    """Parse a month string in YYYY-MM format."""
    return datetime.datetime.strptime(s, '%Y-%m').date()

def parse_amount(s: str):  # https://stackoverflow.com/questions/379906/how-do-i-parse-a-string-to-a-float-or-int
    """Parse a amount str to an int.  12.50 == 1250 pennies"""
    try:
        return int(round(float(s) * 100))
    except (ValueError, TypeError):
        return print("Please enter a Valid amount")
                        


def format_money(pennies: int):
    pounds = Decimal(pennies) / Decimal(100)
    return f"£{pounds:.2f}"




def validate_type(t: str):
  return None

def date_in_range(d: date, start: date, end: date):

    return None
