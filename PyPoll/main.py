import csv
import os

# Function to get the total number of votes cast
def getTotalVotesCast(votesList):
    totalVotes = len(votesList)
    return totalVotes

# Function to get a complete list of candidates who received votes
def getCandidatesList(candidateList):
    candidates = []
    for candidate in candidateList:
        if candidate not in candidates:
            candidates.append(candidate)

    return candidates

# Function to get the percentage of votes each candidate won
def getCandidateVotePercentage(totalVotes, voteCount):
    votePercentage = {}
    for key in voteCount:
        votePercentage[key] = str(round((voteCount[key] / totalVotes) * 100, 3)) + "%"
    return votePercentage

# Function to get the total number of votes each candidate won
def getCandidateVoteCount(voteList):
    candidateVotes = {}
    for candidate in voteList:
        if candidate not in candidateVotes.keys():
            candidateVotes[candidate] = 1
        else:
            candidateVotes[candidate] += 1
    return candidateVotes

# Function to get the winner of the election based on popular vote.
def getElectionWinner(voteCount):
    highestVotes = 0
    winner = ""
    for key in voteCount:
        if voteCount[key] > highestVotes:
            highestVotes = voteCount[key]
            winner = key
    return winner

# Initialize variables
voterIDList = []
countiesList = []
candidateVotesList = []

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
        candidateVotesList.append(row[2])

totalVotes = getTotalVotesCast(voterIDList)
candidates = getCandidatesList(candidateVotesList)
voteCounts = getCandidateVoteCount(candidateVotesList)
votePercentages = getCandidateVotePercentage(totalVotes, voteCounts)
winner = getElectionWinner(voteCounts)

outputLines = []

outputLines.append("Election Results\n")
outputLines.append("----------------------------\n")
outputLines.append(str(f"Total Votes: {totalVotes}\n"))
outputLines.append("----------------------------\n")
for key in voteCounts:
    outputLines.append(str(f"{key}: {votePercentages[key]} ({voteCounts[key]})\n"))
outputLines.append("----------------------------\n")
outputLines.append(str(f"Winner: {winner}\n"))
outputLines.append("----------------------------\n")



filename = 'PyPollResults.txt'
path = 'analysis/'
with open(os.path.join(path, filename), 'w') as file:

    for line in outputLines:
        print(line)
        file.write(line)

