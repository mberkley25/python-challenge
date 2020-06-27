# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    Total_Months = []
    Total_Profit = []

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)


# using a for loop to iterate through a SCV file and increment a counter num_rows

    num_rows = -1

    for row in open(csvpath):
        num_rows += 1

    print(num_rows)

# total  2nd column

    for row in csvreader:

        Total_Profit.append(row[0])
        print(Total_Profit)


# Final Output

print(f""" FINANCIAL ANALYSIS

------------------------------------------------
Total Months: {num_rows} 
Total Profit: {Total_Profit}""")