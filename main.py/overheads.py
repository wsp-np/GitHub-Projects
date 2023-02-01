from pathlib import Path
import csv 

fp= Path.cwd()/"csv_reports"/"overheads-day-90.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    category = []
    value = []

    for x in reader:
        category.append(x[0])
        value.append(float(x[1]))
    
def overhead():
    """
    This finds the highest overhead category and its value when executed. 
    This function does not need parameter.
    """
# create an empty list to store the highest overhead value
    high = []
# for-loop that iterates over overhead value
    for highest in value:
# append the highest overhead value using max() and .append() to the empty list
        high.append(max(value))
# break and stop the for-loop from iterating using break function
        break
# use .index() to identify the index position of the highest overhead value
# create a variable and assign it to the category of the highest overhead value 
    idx = high.index(max(value))
# return the highest overhead in USD, rounded to 1 decimal place using round() and its category in capital letters using .upper() 
    return f"[HIGHEST OVERHEADS] {(category[idx]).upper()}: USD {round(high[0],1)}%"
# execute overhead() function using print function
print(overhead())
