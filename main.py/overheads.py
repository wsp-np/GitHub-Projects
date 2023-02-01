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

    high = []
    for highest in value:
        high.append(max(value))
        break

    idx = high.index(max(value))

    return f"[HIGHEST OVERHEADS] {(category[idx]).upper()}: USD {round(high[0],1)}%"

print(overhead())
