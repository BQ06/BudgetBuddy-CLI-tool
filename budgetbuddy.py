# Used to parse command-line arguments for the Budget Buddy application found at https://docs.python.org/3/library/argparse.html#add-help
import argparse

from models import Transaction

class main:

    def build_parser():
      # Create the top-level parser, inside of parser build_parser function we have defined all parser information
     parser = argparse.ArgumentParser(
       prog='Budget Buddy', 
       description="Budget Buddy - Track your expenses and manage your budget.", 
       exit_on_error=True
       )
      # Create subparsers for different commands
     subparsers = parser.add_subparsers(dest="command", help="Available commands")

     # Add subparsers for each command
     add_parser = subparsers.add_parser("add", help="Add a new transaction")
     add_parser.add_argument("--type", choices=["income", "expense"], help="Type of transaction", type = str)
     add_parser.add_argument("--amount", type=float, help="Amount of the transaction")
     add_parser.add_argument("--category", help="Category of the transaction", type = str)
     add_parser.add_argument("--note", help="Optional note for the transaction", type = str)
     add_parser.add_argument("--date", help="Date of the transaction in YYYY-MM-DD format (default: today)", type = str)
     add_parser.add_argument("--budget", help="Set a monthly budget for a category", type = str)
     

     # View transactions parser to see all transactions or filter by type
     view_parser = subparsers.add_parser("view", help="View transactions")
     view_parser.add_argument("--type", choices=["income", "expense"], help="Filter by transaction type", type = str)

     # Set quit parser to exit application if needed 
     quit_parser = subparsers.add_parser("quit", help="Quit the application")
     quit_parser.add_argument("--confirm", choices=["yes", "no"], help="Confirm quitting the application", type = bool)

     return parser

    def handle_args(args):
      # Handle the parsed arguments and call appropriate functions
      if args.command == "add":
        print("Adding transaction...")
      elif args.command == "view":
        print("Viewing transactions...")
      elif args.command == "quit":
        print("Quitting application...")



def print_transactions_table(txns: list[Transaction]):
    # Print transactions in a formatted table
    print(f"{'ID':<5} {'Type':<10} {'Amount':<10} {'Category':<15} {'Date':<12} {'Note':<20}")
    print("-" * 75)
    for txn in txns:
        print(f"{txn.id:<5} {txn.type:<10} {txn.amount:<10.2f} {txn.category:<15} {txn.date:<12} {txn.note:<20}")


def print_summary(summary: dict):
    # Print budget summary
    print("Budget Summary:")
    for category, data in summary.items():
        print(f"Category: {category}")
        print(f"  Budget: {data['budget']:.2f}")
        print(f"  Spent: {data['spent']:.2f}")
        print(f"  Remaining: {data['remaining']:.2f}")
        print() 
        
  
  