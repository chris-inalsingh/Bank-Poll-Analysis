import csv
import os

#Create file path
bank_data = os.path.join("Resources","budget_data.csv")

#Variables
total_months = 0
total_amount = 0
average_change = []
previous_amount = 0
profit_losses = []
month_list = []

#Read csv file
with open(bank_data) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        #Total number of monthes
        total_months += 1
       
       #Net total amount
        total_amount = total_amount + int(row[1])

        #Average change in Proft/Losses
        profit_losses.append(int(row[1]))
        month_list.append(str(row[0]))
        
for i in range(len(profit_losses)):
    if i == 0:
        previous_amount = profit_losses[i]
    else:
        monthly_change = profit_losses[i] - previous_amount
        average_change.append(monthly_change)
        previous_amount = profit_losses[i]

average = round(sum(average_change)/len(average_change),2)

#Greatest increase in profits & greatest decrease in losses
greatest_increase = max(average_change)
greatest_decrease = min(average_change)


index_increase = average_change.index(greatest_increase) + 1
date_increase = month_list[index_increase]
index_decrease = average_change.index(greatest_decrease) + 1
date_decrease = month_list[index_decrease]

#Print Analysis
print('Financial Analysis')
print('----------------------------')
print(f'Total Monthes: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average}')  
print(f'Greatest Increase in Profits: {date_increase} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {date_decrease} (${greatest_decrease})')
    
        
#Export Analysis
output_file = os.path.join("analysis","analysis.txt")   
with open(output_file, 'w') as datafile:
    datafile.write('Financial Analysis\n')
    datafile.write('----------------------------\n')
    datafile.write(f'Total Monthes: {total_months}\n')
    datafile.write(f'Total: ${total_amount}\n')
    datafile.write(f'Average Change: ${average}\n')  
    datafile.write(f'Greatest Increase in Profits: {date_increase} (${greatest_increase})\n')
    datafile.write(f'Greatest Decrease in Profits: {date_decrease} (${greatest_decrease})\n')
    datafile.close()
    

