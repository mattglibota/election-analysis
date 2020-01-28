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


#open election results file
with open(file_to_load) as election_data:
    
    #To do: perform analysis
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    print(headers)


#using open function with "w" mode, we write data
with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

