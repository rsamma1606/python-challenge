import csv

# Declaring Variables
totalMonths = 0
netTotal = 0
previousMonthProfit = 0
changes = []
greatestIncrease = {"date": "", "amount": 0}
greatestDecrease = {"date": "", "amount": 0}

# Lets read from the CSV PyBank that is supplied under resources
with open("Resources/budget_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # We dont want to read the header row so lets skip it
    next(csvreader)
    
    # Now we read through the CSV
    for row in csvreader:
        # We increment each month
        totalMonths += 1
        
        # Adding our profit/loss to the net total
        netTotal += int(row[1])
        
        # recording change from the previous month
        if totalMonths > 1:
            change = int(row[1]) - previousMonthProfit
            changes.append(change)
            
            # recording greatest increase and decrease
            if change > greatestIncrease["amount"]:
                greatestIncrease["date"] = row[0]
                greatestIncrease["amount"] = change
            elif change < greatestDecrease["amount"]:
                greatestDecrease["date"] = row[0]
                greatestDecrease["amount"] = change
        
        # now we are storing this recording to the previous month variable 
        previousMonthProfit = int(row[1])

# Calculating average changes
averageChange = sum(changes) / len(changes)

# Print our analysis and prepare it for txt file
analysis = (
   "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${netTotal}\n"
    f"Average Change: ${averageChange:.2f}\n"
    f"Greatest Increase in Profits: {greatestIncrease['date']} (${greatestIncrease['amount']})\n"
    f"Greatest Decrease in Profits: {greatestDecrease['date']} (${greatestDecrease['amount']})\n"
)

print(analysis)

# Write to txt file
with open("analysis/PyBank_Analysis.txt", "w") as textfile:
    textfile.write(analysis)
