import csv
import os

#Create Filepath
poll_data = os.path.join("Resources","election_data.csv")

#Variables
total_votes = 0
khan_total = 0
correy_total = 0
li_total = 0
otooley_total = 0

#read csv file
with open(poll_data) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:


        #Calculate total votes
        total_votes += 1

        #total of candidates
        if row[2] == "Khan":
            khan_total += 1
        elif row[2] == "Correy":
            correy_total += 1
        elif row[2] == "Li":
            li_total += 1    
        elif row[2] == "O'Tooley":
            otooley_total += 1
        
        #Calculate percentage of votes
        khan_percent = round(khan_total/total_votes * 100,2)
        correy_percent = round(correy_total/total_votes * 100,2)
        li_percent = round(li_total/total_votes * 100,2)
        otooley_percent = round(otooley_total/total_votes * 100,2)

        #Winner of election
        winner_results=[khan_percent, correy_percent, li_percent, otooley_percent]

        if max(winner_results) == khan_percent:
            winner = "Khan"
        elif max(winner_results) == correy_percent:
            winner = "Correy"
        elif max(winner_results) == li_percent:
            winner = "Li"
        elif max(winner_results) == otooley_percent:
            winner = "O'Tooley" 

#Print Analysis
print('Election Results\n')
print('-------------------------\n')
print(f'Total Votes: {total_votes}\n')
print('-------------------------\n')
print(f'Khan: {khan_percent}% ({khan_total})\n')
print(f'Correy: {correy_percent}% ({correy_total})\n')
print(f'Li: {li_percent}% ({li_total})\n')
print(f"O'Tooley: {otooley_percent}% ({otooley_total})\n")

#Export Analysis
output_file = os.path.join("analysis","analysis.txt")   
with open(output_file, 'w') as datafile:
    datafile.write('Election Results\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Khan: {khan_percent}% ({khan_total})\n')
    datafile.write(f'Correy: {correy_percent}% ({correy_total})\n')
    datafile.write(f'Li: {li_percent}% ({li_total})\n')
    datafile.write(f"O'Tooley: {otooley_percent}% ({otooley_total})\n")
