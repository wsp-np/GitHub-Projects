from pathlib import Path
import csv 

fp= Path.cwd()/"csv_reports"/"cash-on-hand.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    day = []
    coh =[]

    for row in reader:
        day.append(row[0])
        coh.append(float(row[1]))

    x = []
    for x in coh:
        x = coh[0] - coh[1]
    
print(x)