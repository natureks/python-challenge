# Import Dependencies
import os
import csv

def output_str(file_obj, out_str):
    print(out_str)
    summary_file.writelines(out_str + "\n")

# Path to collect data and write summary from the Resources folder
budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')
summary_filename = os.path.join('.', 'Resources', 'budget_data_summary.txt')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    rowCount = 0
    total = 0
    prevProfit = 0
    maxProfitChange = 0
    minProfitChange = 0
    totalChangeInProfit = 0
    
    # Loop through the data
    for row in csvreader:
        if csvreader.line_num == 1:
            continue
        rowCount = rowCount + 1
        currentProfit = int(row[1])
        total = total + currentProfit
        changeInProfit = currentProfit - prevProfit
        if csvreader.line_num != 2:
           totalChangeInProfit = totalChangeInProfit + changeInProfit
        if changeInProfit > maxProfitChange:
            maxProfitChange = changeInProfit
        elif changeInProfit < minProfitChange:
            minProfitChange = changeInProfit
        prevProfit = currentProfit
    
    average=round(totalChangeInProfit/(rowCount-1), 2)


with open(summary_filename, 'w') as summary_file:
    output_str(summary_file, "Financial Analysis")
    output_str(summary_file, "----------------------------")
    output_str(summary_file, f"Total Months: {rowCount}")
    output_str(summary_file, f"Total : {total}")
    output_str(summary_file, f"Average  Change : {average}")
    output_str(summary_file, f"Greatest Increase in Profits : {maxProfitChange}")
    output_str(summary_file, f"Greatest Decrease in Profits : {minProfitChange}")
    


# In[ ]:




