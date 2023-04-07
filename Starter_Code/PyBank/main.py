import os
import csv

# Locate csv file through os.path.join
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Create empty lists to specify specific rows for the following variables
totalmonths = []
totalprofit = []
monthly_profit_change = []
 
# Open csv file
with open(csvpath) as csvfile:

     # Store the contents of budget_data.csv as a varaible
    csvreader = csv.reader(csvfile)

    # Skip the header
    header = next(csvreader)  

    # Read through the rows in csv file
    for row in csvreader: 

        # Append the total months and total profit according to thier specefic lists
        totalmonths.append(row[0])
        totalprofit.append(int(row[1]))

    # check through the profits to get monthly change
    for i in range(len(totalprofit)-1):
        
        # use the difference between the two months and append to monthly profit change
        monthly_profit_change.append(totalprofit[i+1]-totalprofit[i])
        
# Gather max and min of the the montly profits
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to the proper month using month list and index from max and min
# use the plus 1 at the end of months associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(totalmonths)}")
print(f"Total: ${sum(totalprofit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {totalmonths[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {totalmonths[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
output_path = os.path.join('PyBank', 'analysis', "results.txt")
with open(output_path, "w") as file:

# Write methods to print to results.txt
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {len(totalmonths)}\n")
    file.write(f"Total: ${sum(totalprofit)}\n")
    file.write(f"Greatest Increase in Profits: {totalmonths[max_increase_month]} (${(max_increase_value)})\n")
    file.write(f"Greatest Decrease in Profits: {totalmonths[max_decrease_month]} (${(max_decrease_value)})\n")
