#Data we need to retreive
#1. Total number of votes cast
#2. complete list of counties which received votes
#3. percentage of votes each county had
#4. calculate largest county turnout
#5. complete list of candidates who received votes
#6. percentage of votes each candidate won
#7. total number of votes each candidate won
#8. the winner of election based on popular vote

import csv, os

#assign var for the file to load and path
file_to_load = os.path.join("Resources","election_results.csv")
#create filename var to a path to the file
file_to_save = os.path.join("Analysis","election_analysis.txt")

#initialize total votes counter
total_votes = 0

#candidate options
candidate_options = []
candidate_votes = {}

#county metrics initialize
county_list = []
county_votes = {}
largest_county = ""
largest_count = 0
largest_percentage =0

#winning candidate metrics initialize
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open election results file
with open(file_to_load) as election_data:
    #read the file object with reader function
    file_reader = csv.reader(election_data)

    #read the headers row and ignore it
    headers = next(file_reader)

    #loop through each row of csv to gather data
    for row in file_reader:
        #add to total vote count
        total_votes += 1

        ##CANDIDATE GATHER DATA
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            #add name to candidate list
            candidate_options.append(candidate_name)
            #begin tracking vote count
            candidate_votes[candidate_name]=0

        #add votes to appropriate candidate key
        candidate_votes[candidate_name] += 1

        ##COUNTY GATHER DATA
        county_name = row[1]
        if county_name not in county_list:
            #add county to list
            county_list.append(county_name)
            #begin tracking vote count
            county_votes[county_name] = 0

        #add votes to appropriate county key
        county_votes[county_name] +=1

##CALCULATING METRICS AND WRITING TO TEXT FILE
#using open function with "w" mode, we write data to text file
with open(file_to_save,"w") as txt_file:

    ## TOTAL ELECTION METRICS
    #create string with total votes and formatting
    election_results =(
        "Election Results\n"
        "-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        "-------------------------\n\n"
        "County Votes:\n")

    #write election results to terminal and txt file
    print(election_results, end="")
    txt_file.write(election_results)

    ## COUNTY METRICS
    #loop through counties and display votes
    for name in county_votes:
        #calculate vote percentage of each county
        votes = county_votes[name]
        vote_percentage = int(votes) / int(total_votes) *100
        county_results = (f"{name}: {vote_percentage:.1f}% ({votes:,})\n")

        #write county results to terminal and txt file
        print(county_results)
        txt_file.write(county_results)

        #determine largest county
        #is current votes and percentage greater than previous largest
        if (votes > largest_count) and (vote_percentage > largest_percentage):
            largest_count = votes
            largest_percentage = vote_percentage
            largest_county = name

    #create and write largest county to terminal and txt file    
    largest_county_summary = (
        "\n------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        "------------------------\n"
    )
    print(largest_county_summary)
    txt_file.write(largest_county_summary)

    ## CANDIDATE METRICS
    #loop through candidates to calculate metrics
    for name in candidate_votes:

        #calculate vote percentage of each name
        votes = candidate_votes[name]
        vote_percentage = int(votes) / int(total_votes) *100
        candidate_results = (f"{name}: {vote_percentage:.1f}% ({votes:,})\n")

        #write candidate results to terminal and txt file
        print(candidate_results)
        txt_file.write(candidate_results)

        #determine winning vote count and candidate
        #is current votes and percentage greater than previous winner
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

    #write winning candidate to terminal and txt file
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)


