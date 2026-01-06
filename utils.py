import datetime

# https://docs.python.org/3/library/datetime.html#aware-and-naive-objects used for date parsing understanding 

def parse_date(s: str):
    """Parse a date string in YYYY-MM-DD format."""
    return datetime.datetime.strptime(s, '%Y-%m-%d').date()

# datetime.datetime used to convert string to date object
def parse_month(s: str):
    """Parse a month string in YYYY-MM format."""
    return datetime.datetime.strptime(s, '%Y-%m').date()

def parse_
