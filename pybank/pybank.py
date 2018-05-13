
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
    average_revenue_change = (sum(revenue_change)/total_months)
    total_revenue_print = ("Total revenue:" + str(total_revenue))
    total_months_print = ("Total months" + ": " + str(total_months))
    average_revenue_print = ("Average Revenue Change:" + str(average_revenue_change))
    #print("Financial Analysis")
    #print("__________________________________________________________")
    #print(total_months_print)
    #print(total_revenue_print)
    #print(average_revenue_print)
    Greatest_increase_revenue = (("Greatest Increase in Revenue:" + date_list[revenue_change.index(max(revenue_change)) ] + " " + str(max(revenue_change))))
    #print(Greatest_increase_revenue)
    Greatest_decrease_revenue = (("Greatest Decrease in Revenue:" + date_list[revenue_change.index(min(revenue_change)) ] + " " + str(min(revenue_change))))
    #print(Greatest_decrease_revenue)
output = (
    f"Financial Analysis\n"
    f"__________________________________________________________\n"
    f"{total_months_print}\n"
    f"{total_revenue_print}\n"
    f"{average_revenue_print}\n"
    f"{Greatest_increase_revenue}\n"
    f"{Greatest_decrease_revenue}\n")
print(output)
file = open("finacial_analysis.txt","w")
file.write(output)