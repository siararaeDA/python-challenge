import csv
import os

# Your task is to create a Python script that analyzes the votes and calculates each of the following:


# The total number of votes cast


# A complete list of candidates who received votes


# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote.

# Initialize variables
voterIDList = []
countiesList = []
candidatesList = []

csvpath = os.path.join('Resources', 'election_data.csv')
# Add this to the path to run from a different folder: os.path.dirname(__file__), 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # Create an array of Voter IDs
        voterIDList.append(row[0])
        # Create an array of counties
        countiesList.append(row[1])
        # Create an array of candidates
        candidateList.append(row[2])

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
