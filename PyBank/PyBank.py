import os
import csv 
# Create analysis function
def analyze_budgets(file):

    # Declare variables 
    total_months = 0
    total_profit = 0
    greatest_inc = 0
    greatest_inc_month = ""
    greatest_dec = 0
    greatest_dec_month = ""
    # prev_pl (profit/loss) tracks the profit/loss of the previous month (for the changes variable)
    prev_pl = 0

    # keeps a running total of change on a monthly basis
    changes = []
           # Open csv and read with csv reader
    with open(file) as data:
        csvreader = csv.reader(data, delimiter = ',')
        #save header row
        header = next(csvreader)
        # Create the 'for' loop to loop through each row in budget_data.csv
        for row in csvreader:
            date = row[0]
            pl = int(row[1])
            # Keep running total of total profit
            total_profit += pl

            # Add one to the count of total months to get total number of months used in the dataset
            total_months += 1

            # Subtract the previous month's pl from the current month;
            # if this is the first month, discard the value. If this is
            # not the first month, append the change to the changes list.

            #Since the change variable keeps a running total of the profit/loss
            #on a monthly basis, need to find the difference between the previous
            #month pl and the current month pl for all months except the first
            #month (because there is no data to compare the first month to. Can
            #only begin comparing data starting with month 2 because you can
            #compare it to month 1.)
            change = pl - prev_pl
            if total_months != 1:
                changes.append(change)

            #If the monthly change in profit is greater than the greatest increase,
            #use the change variable so it will add to the total net profit/loss. If the
            #monthly change in profit is less than the greatest decrease, then use the 
            #change variable so it will subtract from the total net profit/loss
            if change > greatest_inc:
                greatest_inc = change
                greatest_inc_month = date
            if change < greatest_dec:
                greatest_dec = change
                greatest_dec_month = date

            # Replace prev_pl with pl for next loop
            prev_pl = pl
            
    # Calculate average change 
    avg_change = round(sum(changes)/len(changes), 2)

    # Following line was deprecated due to clarity on instructions.
    # monthly_avg_profit = int(round(total_profit/total_months, 0))

  #Create a string for printing and save as a text file
    analysis = f"""
    Total Profit: ${total_profit}
    Total Months: {total_months}
    Average Monthly Change: ${avg_change}
    Greatest Increase: {greatest_inc_month}, ${greatest_inc}
    Greatest Decrease: {greatest_dec_month}, ${greatest_dec}
    """
    # Print the final analysis
    print(analysis)
    # Create a text file using the final analysis
    output_file = "output.txt"
    with open(output_file, "w") as doc:
        doc.write(analysis)
#Create file path for csv import
path = os.path.join("Resources", "budget_data.csv")
# Run the function on the path
analyze_budgets(path)









