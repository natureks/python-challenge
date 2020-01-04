#!/usr/bin/env python

# Import Dependencies
import os
import csv


# Path to collect data from the Resources folder
budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')


# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    rowCount = 0
    total = 0
    prevProfit = 0
    maxProfitChange = 0
    minProfitChange = 0
    average = 0
    
    # Loop through the data
    for row in csvreader:
        rowCount = rowCount + 1
        currentProfit = int(row[1])
        total = total + currentProfit
        changeInProfit = currentProfit - prevProfit
        if changeInProfit > maxProfitChange:
            maxProfitChange = changeInProfit
        elif changeInProfit < minProfitChange:
            minProfitChange = changeInProfit
        prevProfit = currentProfit
    
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {rowCount}")
    print(f"Total : {total}")
    print(f"Average  Change : {average}")
    print(f"Greatest Increase in Profits : {maxProfitChange}")
    print(f"Greatest Decrease in Profits : {minProfitChange}")

        
