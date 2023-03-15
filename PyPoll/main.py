import csv

# Path to the csv
file_path = "Resources/election_data.csv"

# declare variables
totalVotes = 0
candidates = {}
winnerVotes = 0
winnerName = ""

# Now we read through the CSV
with open(file_path, "r") as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    # we loop through the CSV rows
    for row in csvreader:
        # we increment the total number of votes
        totalVotes += 1
        
        # we add the candidate the the array of candidates
        candidateName = row["Candidate"]
        if candidateName in candidates:
            candidates[candidateName] += 1
        else:
            candidates[candidateName] = 1

# Print election results 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")

for candidate, votes in candidates.items():
    # Calculating the percentage of votes each candidate won
    votePercentage = round(votes / totalVotes * 100, 3)
    
    # Print the candidate's name, percentage of votes, and number of votes
    print(f"{candidate}: {votePercentage}% ({votes})")
    
    # Check if this candidate is the winner
    if votes > winnerVotes:
        winnerName = candidate
        winnerVotes = votes

print("-------------------------")
print(f"Winner: {winnerName}")
print("-------------------------")

# Write the resultds to txtfile
with open("analysis/PyPoll_Results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {totalVotes}\n")
    txtfile.write("-------------------------\n")
    # we need to also include this for loop during the txtfile writing stage
    for candidate, votes in candidates.items():
        
        votePercentage = round(votes / totalVotes * 100, 3)

        txtfile.write(f"{candidate}: {votePercentage}% ({votes})\n")

    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winnerName}\n")
    txtfile.write("-------------------------\n")
