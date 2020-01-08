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
    total = 0
    prevProfit = 0
    maxProfitChange = 0
    minProfitChange = 0
    totalChangeInProfit = 0
    maxProfitDate = ""
    minProfitDate = ""
    
    # Loop through the data
    for row in csvreader:
        if csvreader.line_num == 1:
            continue
        currentProfit = int(row[1])
        total = total + currentProfit
        changeInProfit = currentProfit - prevProfit
        if csvreader.line_num != 2:
           totalChangeInProfit = totalChangeInProfit + changeInProfit
        if changeInProfit > maxProfitChange:
            maxProfitChange = changeInProfit
            maxProfitDate = row[0]
        elif changeInProfit < minProfitChange:
            minProfitChange = changeInProfit
            minProfitDate = row[0]
        prevProfit = currentProfit
    
    rowCount = csvreader.line_num - 1
    average=round(totalChangeInProfit/(rowCount-1), 2)

summary_filename = os.path.join('.', 'Resources', 'budget_data_summary.txt')
with open(summary_filename, 'w') as summary_file:
    output_str(summary_file, "Financial Analysis")
    output_str(summary_file, "----------------------------")
    output_str(summary_file, "Total Months: {0:.0f}".format(rowCount))
    output_str(summary_file, "Total : ${0:,.2f}".format(total))

    output_str(summary_file, "Average  Change : ${0:,.2f}".format(average))
    output_str(summary_file, f"Greatest Increase in Profits: {maxProfitDate} ${maxProfitChange}")
    output_str(summary_file, f"Greatest Decrease in Profits: {minProfitDate} ${minProfitChange}")



