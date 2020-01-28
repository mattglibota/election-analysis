#Data we need to retreive
#1. Total number of votes cast
#2. complete list of candidates who received votes
#3. percentage of votes each candidate won
#4. total number of votes each candidate won
#5. the winner of election based on popular vote

import csv, os

#assign var for the file to load and path
file_to_load = os.path.join("Resources","election_results.csv")
#create filename vari to a path to the file
file_to_save = os.path.join("Analysis","election_analysis.txt")
#read the file object with reader function

#initialize total votes counter
total_votes = 0

#candidate options
candidate_options = []
candidate_votes = {}

#winning candidate tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open election results file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    for row in file_reader:
        #add to total vote count
        total_votes += 1

        #print candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:

            #add name to candidate list
            candidate_options.append(candidate_name)
            #begin tracking vote count
            candidate_votes[candidate_name]=0

        candidate_votes[candidate_name] += 1

#loop through candidates to calculate metrics
for name in candidate_votes:

    #calculate vote percentage of each name
    votes = candidate_votes[name]
    vote_percentage = int(votes) / int(total_votes) *100
    print(f"{name}: {vote_percentage:.1f}% ({votes:,})\n")

    #determine winning vote count and candidate
    #is current votes and percentage greater than current winner
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = name

#create winning candidate statement
winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------\n")
print(winning_candidate_summary)


#using open function with "w" mode, we write data
with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

