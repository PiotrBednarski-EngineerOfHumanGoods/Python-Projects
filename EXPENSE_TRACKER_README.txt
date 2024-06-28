# Monthly Expenses Tracker

This Python script calculates the total expenses for a given month from a CSV file and updates a JSON file with the total expenses for each month.

## Features
- Reads transactions from a CSV file.
- Calculates the total expenses for a specified month.
- Updates or creates a JSON file to store the total monthly expenses.

## Requirements
- Python 3.x

## Usage

1. **Prepare your CSV file**: Ensure your CSV file is named `Transactions.csv` and has the following headers:
   - `Date` (format: YYYY-MM-DD)
   - `Amount` (transaction amount, e.g., 1000.00 or 1,000.00)
   - `Transaction Type` (e.g., Debit or Credit)

2. **Run the script**: Execute the script in your terminal or command prompt.

```bash
python monthly_expenses_tracker.py
