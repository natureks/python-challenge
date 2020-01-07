# Import Dependencies
import os
import csv

def output_str(file_obj, out_str):
    print(out_str)
    summary_file.writelines(out_str + "\n")

# Path to collect data from the Resources folder
election_data_file = os.path.join('.', 'Resources', 'election_data.csv')
election_summary_file = os.path.join('.', 'Resources', 'election_data_summary.txt')

# Read in the CSV file
with open(election_data_file, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    votes = []
    candidates = {}
    
    # Loop through the data
    for row in csvreader:
        if csvreader.line_num == 1:
            continue
        votes.append(row[2])
        candidates[row[2]] = 0

    rowCount = csvreader.line_num - 1
    
    for candidate in candidates.keys():
        candidates[candidate] = votes.count(candidate)

with open(election_summary_file, 'w') as summary_file:
    output_str(summary_file, "----------------------------")
    output_str(summary_file, "Election Results")
    output_str(summary_file, "----------------------------")
    output_str(summary_file, f"Total Votes: {rowCount}")
    output_str(summary_file, "----------------------------")
    winner = ""
    winner_vote = 0
    for candidate, vote in candidates.items():
        if vote > winner_vote:
            winner_vote = vote
            winner = candidate
        percent = round(vote*100/rowCount, 3)
        output_str(summary_file, f"{candidate}: {percent}% ({vote})")
        
    output_str(summary_file, "----------------------------")
    output_str(summary_file, f"Winner : {winner}")
    output_str(summary_file, "----------------------------")
