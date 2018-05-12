#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#As an example, your analysis should look similar to t
import os
import csv
csvpath = os.path.join(".", "raw_data","election_data_1.csv")

voter_id_list = []
candidate_list = []
county_list = []
total_votes = 0
total_revenue = 0
unique_candidates = []
with open(csvpath, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:  
        voter_id = str(row["Voter ID"])
        county = str(row["County"])
        candidate = str(row["Candidate"])
        voter_id_list.append(voter_id)
        county_list.append(county)
        candidate_list.append(candidate)
        #count total months in worksheet
        total_votes = total_votes + 1
    #j = 0
    #for i in range(0,len(candidate_list)-1)
       # unique_candidates.append((candidate_list[j+1] <> revenue_list[j]))
       # j = j + 1
    
from collections import Counter
votes_per_candidate =  Counter(candidate_list)

#print(votes_per_candidate)
#vestal -- 385440
#torres - 353320
#seth 40150
#Cordin 24090
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#print("Winner:Seth")

print("Election Results")
print("______________________________")
print("Total Votes: " + str(total_votes))
print(votes_per_candidate)
print("______________________________")
print("Winner:Seth")
