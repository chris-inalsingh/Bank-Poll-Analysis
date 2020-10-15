import csv
import os

bank_data = os.path.join("Resources","budget_data.csv")

#Variables
total_months = 0
total_amount = 0
amount_change = 0
previous_amount = 0
amount_change_list = []
amount_change = 0
month_of_change = []



with open(bank_data) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        
        total_months += 1
       
        total_amount = total_amount + int(row[1])
    
        amount_change = float(row[1])- previous_amount
        previous_amount = float(row[1])
        amount_change_list = amount_change_list + [amount_change]
        
        average = sum(amount_change_list)/len(amount_change_list)
    
        

print(average)



#output_file = os.path.join("analysis")
    
#with open(output_file) as datafile:
   # datafile.write("Financial Analysis\n")
   # datafile.write("---------------------\n")
    #datafile.write("Total Months: %d\n" % total_months)



