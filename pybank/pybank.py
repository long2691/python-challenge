import os
import csv
#Total Months: 25
#Total Revenue: $1241412
#Average Revenue Change: $216825
#Greatest Increase in Revenue: Sep-16 ($815531)
#Greatest Decrease in Revenue: Aug-12 ($-652794)

csvpath = os.path.join(".", "raw_data","budget_data_1.csv")
#The total number of months included in the dataset
#read data into a dictionary and create an email

date_list = []
total_months = 0
total_revenue = 0
revenue_list = []
revenue_change = []
with open(csvpath, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:  
        date = str(row["Date"])
        revenue = int(row["Revenue"])
        date_and_revenue = date + " " + "($" + str(revenue) + ")"
        #count total months in worksheet
        total_months = total_months + 1
        #add total revenue in worksheet
        total_revenue = total_revenue + revenue
        #append revenue to list in order to use indexes
        revenue_list.append(revenue)
          #append revenue to list in order to use indexes
        date_list.append(date)
    #revenue change
    j = 0
    for i in range(0,len(revenue_list)-1):    
        revenue_change.append((revenue_list[j+1] - revenue_list[j]))
        j = j + 1
    #Your final script must be able to handle any such similarly structured dataset in the future (your boss is going to give you more of these -- so your script has to work for the ones to come). In addition, your final script should both print the analysis to the terminal and export a text file with the results.
    #print(revenue_change)
    #print greatest increase
    #print(date_list)
    print(date_list[revenue_change.index(max(revenue_change)) ] + " " + str(max(revenue_change)))
    #print greatest decrease
    #print(max(revenue_change))

    print(date_list[revenue_change.index(min(revenue_change)) ] + " " + str(min(revenue_change)))
    print(str(date_list[0]) + " " +  str(revenue_list[1]))


  


