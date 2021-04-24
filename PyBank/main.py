# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('', 'Resources', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    totalProfit = 0
    numMonths = 0
    currentProfit = 0
    prevProfit = 0
    diffProfit = 0
    amountDecrease = 0
    decreaseCount = 0
    amountIncrease = 0
    increaseCount = 0
    greatestIncrease = 0
    greatestDecrease = 0

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    print("CSV Header: " + str(csv_header))

    for row in csvreader:
        totalProfit += int(row[1])
        numMonths += 1
        
        prevProfit = currentProfit
        currentProfit = int(row[1])
        diffProfit = int(currentProfit) - int(prevProfit)
        if diffProfit < 0:
            amountDecrease = diffProfit
        else:
            amountIncrease = diffProfit
        
        if amountDecrease < int(greatestDecrease):
            decreaseCount+=1
            totalDecrease = row
        else:
            increaseCount+=1
            totalIncrease = row

    average = (float(amountIncrease/increaseCount)+float(amountIncrease/increaseCount)) / 2
    
    print ("Profit & Loss Report: ")
    print ("--------------------- ")
    print ("")
    print ("Month Count:" + str(numMonths))
    print ("Profit / Loss Total: " + str(totalProfit))
    print ("Average: " + str(average))
    print ("Greatest Increase in Profits:"+str(totalIncrease))
    print ("Greatest Decrease in Profits:"+str(totalDecrease))
