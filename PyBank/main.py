import csv
import os

# Function to find the total number of months in the dataset
def getTotalMonths(monthsList):
     totalMonths = len(monthsList)
     return totalMonths

# Function to find the net total of Profit/Losses (column 2) over the entire period.
def getTotalProfitLosses(profLossList):
    totalProfitsLosses = sum(profLossList)
    return totalProfitsLosses

# Function to find the average of the changes in Profit/Losses over the entire period.
def getAverageProfitsLosses(profLossList):
    total = getTotalProfitLosses(profLossList)
    average = total / len(profLossList)
    return average

# Find the greatest increase in profits (date and amount) over the entire period.

# Find the greatest decrease in losses (date and amount) over the entire period.

# Initialize variables
monthsList = []
profitsLossesList = []
bankDataDict = {}

# Read in the data
csvpath = os.path.join(os.path.dirname(__file__), 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

        # Create an array of months
        monthsList.append(row[0])
        # Create an array of profits/losses
        profitsLossesList.append(int(row[1]))
        # Create a dictionary of the data
        bankDataDict[row[0]] = row[1]

# Output
totalMonths = getTotalMonths(monthsList)
profLossSum = getTotalProfitLosses(profitsLossesList)
avgProfLoss = getAverageProfitsLosses(profitsLossesList)

print(f"Total Months: {totalMonths}")
print(f"Total: {profLossSum}")
print(f"Average Change: {avgProfLoss}")

# Example output:
#
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

# Print analysis to the terminal and to a text file