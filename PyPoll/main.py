import csv
import os

# Your task is to create a Python script that analyzes the votes and calculates each of the following:


# Function to get the total number of votes cast
def getTotalVotesCast(votesList):
    totalVotes = len(votesList)
    return totalVotes

# A complete list of candidates who received votes
def getCandidatesList(candidateList):
    candidates = []
    for candidate in candidateList:
        if candidate not in candidates:
            candidates.append(candidate)

    return candidates

# The percentage of votes each candidate won
def getCandidateVotePercentage(totalVotes, voteCount):
    votePercentage = {}
    for key in voteCount:
        votePercentage[key] = round((voteCount[key] / totalVotes) * 100, 3)
    return votePercentage

# The total number of votes each candidate won
def getCandidateVoteCount(voteList):
    candidateVotes = {}
    for candidate in voteList:
        if candidate not in candidateVotes.keys():
            candidateVotes[candidate] = 1
        else:
            candidateVotes[candidate] += 1
    return candidateVotes

# The winner of the election based on popular vote.
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
print(totalVotes)
print(candidates)
print(getCandidateVoteCount(candidateVotesList))
print(getCandidateVotePercentage(totalVotes, voteCounts))
print(getElectionWinner(voteCounts))


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
