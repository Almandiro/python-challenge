# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('', 'Resources', 'budget_data.csv')
file_to_output = os.path.join('', 'Analysis', 'initReport.txt')

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
    
    
    
    with open(file_to_output, "w") as txt_file:
        
        #stringToFile = "Financial Analysis \n --------------------- \n\n Month Count:",str(numMonths)m"Profit / Loss Total: ",str(totalProfit), "Average: ",str(average),"Greatest Increase in Profits:",str(totalIncrease),"Greatest Decrease in Profits:",str(totalDecrease)
                        
        print ("Financial Analysis: ")
        txt_file.write("Financial Analysis: \n")
        print ("--------------------- ")
        txt_file.write("--------------------- \n")
        print ("")
        txt_file.write("\n")
        print ("Month Count:" + str(numMonths))
        txt_file.write("Month Count:" + str(numMonths)+"\n")
        print ("Profit / Loss Total: " + str(totalProfit))
        txt_file.write("Profit / Loss Total: " + str(totalProfit)+"\n")
        print ("Average: " + str(average))
        txt_file.write("Average: " + str(average)+"\n")
        print ("Greatest Increase in Profits:"+str(totalIncrease))
        txt_file.write("Greatest Increase in Profits:"+str(totalIncrease)+"\n")
        print ("Greatest Decrease in Profits:"+str(totalDecrease))
        txt_file.write("Greatest Decrease in Profits:"+str(totalDecrease)+"\n")