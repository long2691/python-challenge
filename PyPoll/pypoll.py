#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#As an example, your analysis should look similar to t
import os
import csv
csvpath = os.path.join(".", "raw_data","election_data_1.csv")
election_results = "election_analysis.txt"
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
for x in candidate_list:
       if x not in unique_candidates:
           unique_candidates.append(x)
    
Candidate_votes = []  
for candidate in unique_candidates:
    word_count = candidate_list.count(candidate)  # Pythons count function, count()
    Candidate_votes.append((candidate,word_count))       
cand_dict = dict(Candidate_votes)
#print(cand_dict)
percent_dict = {}
for key,values in cand_dict.items():
    percent_dict[key]=values/total_votes*100
#print(percent_dict)
maximum = max(percent_dict, key=percent_dict.get) 
#print(maximum)
#for i,j in cand_dict.items()
    #rounded_percent = round(j/total_votes)*100,1)
#rounded_percent
#print(rounded_percent)
output = (
        f"Election Results\n"
        f"______________________________\n"
        f"Total Votes: {candS_dict}\n"
        f"Percent Votes: {percent_dict}\n"
        f"Winner : {maximum}\n")
print(output)
file = open("election_results.txt","w")
file.write(output)