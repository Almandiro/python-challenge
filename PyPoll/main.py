################################################################################
########################## START OF CODE #######################################
################################################################################

# IMPORT PACKAGES
import csv
import os

# DEFINE TEXT READ & WRITE PATHS
csvpath = os.path.join('', 'Resources', 'election_data.csv')
file_to_output = os.path.join('', 'Analysis', 'initReport.txt')

total_votes = 0

candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0

with open(csvpath) as election_data:

    reader = csv.reader(election_data)
    header = next(reader)
 
    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        
# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        "\n\nElection Results\n"
        "-------------------------\n"
        "Total Votes: "+str(total_votes)+"\n"
        "-------------------------\n")
    
    print(election_results)

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = candidate+": "+str(vote_percentage)+"%  "+str(votes)+"\n"
        #print(voter_output, end="")
        print(voter_output)

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        "-------------------------\n"
        "Winner: "+str(winning_candidate)+"\n"
        "-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
