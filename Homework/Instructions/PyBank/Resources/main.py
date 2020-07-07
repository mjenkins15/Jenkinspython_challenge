# Import modules
import os
import csv

def getthestuff(csv):
    months = 0
    total = 0
    maxrev = 0
    minrev = 0
    avgchange = 0
    maxmonth = ""
    minmonth = ""
    lastmonth = None
    changes = []
    for row in csv:
        current_month = row[0]
        current_pnl = int(row[1])
        total += current_pnl
        months += 1
        if lastmonth is not None:
            current_change = current_pnl-lastmonth
            changes.append(current_change)
            if current_change > maxrev:
                maxrev = current_change
                maxmonth = current_month
            if current_change < minrev:
                minrev = current_change
                minmonth = current_month

        lastmonth = current_pnl
    avgchange = sum(changes)/len(changes)
    return [months, total, maxrev, minrev, avgchange, maxmonth, minmonth]

with open("budget_data.csv") as file:
    csvreader = csv.reader(file, delimiter = ',')
    header = next(csvreader)
    analysis = getthestuff(csvreader)
print(f"""
Financial Analysis
-----------------
Total Months: {analysis[0]}
Total: ${round(analysis[1], 2)}
Average Change: ${round(analysis[4], 2)}
Greatest Increase: {analysis[5]} (${analysis[2]})
Greatest Decrease: {analysis[6]} (${analysis[3]})
""")

arr = [2, 4, 34, 6, 21, 18, 24, 29, 31, 18, 48]

arr

def sort_array(arr):
  sorted = []
  for value in arr:
    if len(sorted) == 0:
      sorted.append(value)
    else:
      i = 0
      for ind in sorted:
        if value > ind:
          i+=1
        else:
          sorted.insert(i-1, value)
          break
        if i == len(sorted):
          sorted.append(value)
          break
  return sorted

sort_array(arr)
# Set output file path
# Save the stuff to a text file