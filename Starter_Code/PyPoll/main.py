import os
import csv 

# create path to csv file
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

# list variables 
totalVotes = 0
StockhamVotes = 0
DeGetteVotes = 0
DoaneVotes = 0

# Open csv in default read mode with context manager
with open(csvpath) as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections) 

    # Skip the header to read values
    header = next(csvreader)     

    # Check through each row in the csv
    for row in csvreader: 

        # Count the unique voters id's and store them as a Varible (TotalVotes)
        totalVotes +=1

        # Count each the amount of time each participant names appear
        # Adds one value for every name counted with differnt unique varibles
        if row[2] == "Charles Casper Stockham": 
            StockhamVotes +=1
        elif row[2] == "Diana DeGette":
           DeGetteVotes  +=1
        elif row[2] == "Raymon Anthony Doane": 
            DoaneVotes +=1
        

 # To choose a winner we create both our list into varaibles
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [StockhamVotes, DeGetteVotes ,DoaneVotes]

# zip them together the list of candidates and total votes
# using a max function of the dictionary, we can find thew winner
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a summary of the analysis
StockhamPercent = (StockhamVotes/totalVotes) *100
DeGettePercent = (DeGetteVotes/totalVotes) * 100
DoanePercent = (DoaneVotes/totalVotes)* 100


# Print summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {totalVotes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {StockhamPercent:.3f}% ({StockhamVotes})")
print(f"Diana DeGette: {DeGettePercent:.3f}% ({DeGetteVotes})")
print(f"Raymon Anthony Doane: {DoanePercent:.3f}% ({DoaneVotes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Assign output file location
outputfile = os.path.join("PyPoll", "analysis", "results.txt")

with open(outputfile,"w") as file:

# Write methods to print to results.txt
    file.write(f"Election Results\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Votes: {totalVotes}\n")
    file.write(f"----------------------------\n")
    file.write(f"Charles Casper Stockham: {StockhamPercent:.3f}% ({StockhamVotes})\n")
    file.write(f"Diana DeGette: {DeGettePercent:.3f}% ({DeGetteVotes})\n")
    file.write(f"Raymon Anthony Doane: {DoanePercent:.3f}% ({DoaneVotes})\n")
    file.write(f"----------------------------\n")
    file.write(f"Winner: {key}\n")
    file.write(f"----------------------------\n")