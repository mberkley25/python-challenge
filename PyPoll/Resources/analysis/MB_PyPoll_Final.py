# Import Dependencies

import os

import csv


# Declare file location through pathlib
csv_file = os.path.join('..', 'Resources', 'election_data.csv')

# Create empty lists to iterate through specific rows for the following variables
total_votes = []
khan_votes = []
correy_votes = []

 
# Open csv in default read mode with context manager
with open(csv_file) as election_data:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(election_data,delimiter=",") 

    # Skip the header labels to iterate with the values
    header = next(csvreader)  

    # Iterate through the rows in the stored file contents
    for row in election_data: 

        # Append the total months and total profit to their corresponding lists
        total_votes.append(row[0])
        khan_votes.append(int(row[2]))
        correy_votes.append(int(row[2]))

    for row in election_data:

         if row == "Khan":
                khan_votes.values = khan_votes + 1



# Print Statements

print("Election Results")
print("----------------------------")
print(f"Total Votes: {len(total_votes)}")
print("----------------------------")
print(f"Khan Votes: {sum(khan_votes)}")
print(f"Khan Votes: {sum(khan_votes)/len(total_votes)}")
print("----------------------------")



