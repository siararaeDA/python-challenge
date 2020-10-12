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
    totalChange = 0

    for i in range(1, len(profLossList)):
        totalChange += profLossList[i] - profLossList[i - 1]
    
    average = totalChange / (len(profLossList) - 1)
    return round(average, 2)

# Find the greatest increase in profits (date and amount) over the entire period.
def getGreatestIncreaseProfits(profLossList, monthsList):
    greatestChange = 0
    index = 0

    # Find greatest increase
    for i in range(1, len(profLossList)):
        change = profLossList[i] - profLossList[i - 1]
        if change > greatestChange:
            greatestChange = change
            index = i
    
    # Find the month to match the increase
    month = monthsList[index]

    # Turn into a string to return
    greatestIncreaseInfo = month + " ($" + str(greatestChange) + ")"

    return greatestIncreaseInfo

# Find the greatest decrease in losses (date and amount) over the entire period.
def getGreatestDecreaseProfits(profLossList, monthsList):
    greatestChange = 0
    index = 0

    # Find greatest increase
    for i in range(1, len(profLossList)):
        change = profLossList[i] - profLossList[i - 1]
        if change < greatestChange:
            greatestChange = change
            index = i
    
    # Find the month to match the increase
    month = monthsList[index]

    # Turn into a string to return
    greatestDecreaseInfo = month + " ($" + str(greatestChange) + ")"

    return greatestDecreaseInfo

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
greatestIncreaseProfits = getGreatestIncreaseProfits(profitsLossesList, monthsList)
greatestDecreaseProfits = getGreatestDecreaseProfits(profitsLossesList, monthsList)

# Print analysis to the terminal and to a text file

line1 = "Financial Analysis\n"
line2 = "----------------------------\n"
line3 = str(f"Total Months: {totalMonths}\n")
line4 = str(f"Total: ${profLossSum}\n")
line5 = str(f"Average Change: ${avgProfLoss}\n")
line6 = str(f"Greatest Increase in Proifts: {greatestIncreaseProfits}\n")
line7 = str(f"Greatest Decrease in Profits: {greatestDecreaseProfits}\n")

outputLines = [line1, line2, line3, line4, line5, line6, line7]

filename = 'Results.txt'
with open(filename, 'w') as file:
    for line in outputLines:
        print(line)
        file.write(line)
