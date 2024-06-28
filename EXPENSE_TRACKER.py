import csv
import json
import os
from datetime import datetime

# Function to sum expenses for a given month from the CSV file
def sum_expenses_for_month(csv_file_path, month):
    total_expenses = 0.0
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"The file {csv_file_path} does not exist.")
    
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            try:
                date = row['Date']
                amount = row['Amount'].replace(',', '')
                transaction_type = row['Transaction Type']
                transaction_date = datetime.strptime(date, '%Y-%m-%d')
                if transaction_date.strftime('%Y-%m') == month and transaction_type.lower() == 'debit':
                    total_expenses += float(amount)
            except (ValueError, KeyError) as e:
                print(f"Skipping row due to error: {e}")
                continue  # Skip rows with invalid data or missing columns

    return total_expenses

# Function to update or create the JSON file with total expenses for the month
def update_expenses_json(json_file_path, month, total_expenses):
    expenses_data = {}
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            try:
                expenses_data = json.load(json_file)
            except json.JSONDecodeError as e:
                print(f"Error reading JSON file: {e}")

    # Update the expenses data with the new total for the month
    expenses_data[month] = total_expenses

    # Write the updated data back to the JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(expenses_data, json_file, indent=4)

# Main program
if __name__ == "__main__":
    month_input = input("Please enter the month (format YYYY-MM): ")

    csv_file_name = 'Transactions.csv'
    json_file_name = 'monthly_expenses.json'

    try:
        total_month_expenses = sum_expenses_for_month(csv_file_name, month_input)
        print(f"Total expenses for {month_input}: {total_month_expenses}")
        update_expenses_json(json_file_name, month_input, total_month_expenses)
        print(f"Updated {json_file_name} with total expenses for {month_input}.")
    except Exception as e:
        print(f"An error occurred: {e}")
