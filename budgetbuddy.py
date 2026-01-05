# Used to parse command-line arguments for the Budget Buddy application found at https://docs.python.org/3/library/argparse.html#add-help
import argparse

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
     add_parser.add_argument("type", choices=["income", "expense"], help="Type of transaction", type = str)
     add_parser.add_argument("amount", type=float, help="Amount of the transaction")
     add_parser.add_argument("category", help="Category of the transaction", type = str)
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
