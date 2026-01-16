# BudgetBuddy-CLI-tool
First full python project, did a v1 using just copilot then use of LLMS for feedback and any fixes

SUMMARY:

BudgetBuddy is a command line budgeting tool written in Python that allows users to track income and expenses, store transactions locally, and generate summaries over time.

The project was built to practice core Python fundamentals including:
•	dataclasses and typing
•	argparse for CLI interfaces
•	file-based persistence using JSON
•	date and money handling
•	separation of concerns (CLI, utils, models, service/storage layers)

This is intentionally a CLI-only project to focus on backend logic and correctness rather than UI (also not fully confident on FE dev yet)

How to use:

1. Main features are ADD, VIEW, DELETE, SET_BUDGET, SUMMARY AND QUIT.

2. All commands can be explained using --h or --help flags: 

python3 budgetbuddy.py <Commandname> -h

3. Data is stored locally in a JSON file inside the home directory where budgetbuddy files are stored. 

4. Command Examples: 

ADD = Adds a new transaction to the budget tracker. Used to record income or expenses with an amount, category, optional note, and date.

python3 budgetbuddy.py add --type expense --amount 12.50 --category food --note "Lunch" --date 2026-01-15


VIEW =  Displays stored transactions, with optional filters.

Transactions can be filtered by:

•	transaction type (income / expense)
•	category
•	date range

python3 budgetbuddy.py view
python3 budgetbuddy.py view --type expense --category food
python3 budgetbuddy.py view --from 2026-01-01 --to 2026-01-31

DELETE = Removes a transaction by its ID. This permanently deletes the selected transaction from storage. 

python3 budgetbuddy.py delete 3 = removes id 3 from the list.


SET_BUDGET = Sets a monthly budget for a given category.

python3 budgetbuddy.py set_budget --category food --monthly 300


SUMMARY = Generates total of income from any given range. Includes total income and expenses.

python3 budgetbuddy.py summary
python3 budgetbuddy.py summary --from 2026-01-01 --to 2026-01-31


QUIT =  Quits from the application (not really utilized in terminal so not really working)

python3 budgetbuddy.py quit --yes


5. Future implementations: 

1. Excel/XLSX import and export for transactions and summaries.
2. Possible packaging as imported cli tool?
3. Unit tests