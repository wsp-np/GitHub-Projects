from pathlib import Path
import csv 

# create a file to csv file
fp = Path.cwd()/"csv_reports"/"profit-and-loss.csv"

# read the csv file to append profit and loss from the csv file
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

# append accumulated profit and days as a list back to each empty list
    listofaccumulatedprofits = []
    listofdays = []
    for row in reader:
        listofaccumulatedprofits.append(int(row[4]))
        listofdays.append(int(row[0]))

def profitandloss():
    day0 = listofaccumulatedprofits[0]
    deficit = False
    deficitdays = []
    # use for loop
    for i in range(len(listofaccumulatedprofits)-1):
        difference = listofaccumulatedprofits[i+1] - day0
        if difference < 0:
            deficitdays.append(f"[PROFIT DEFICIT] DAY: {listofdays[i+1]}, AMOUNT: USD{round(difference,1)}")
            deficit = True
        day0 = listofaccumulatedprofits[i+1]
    if deficit == False:
        deficitdays.append(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY.")
    return deficitdays
for i in profitandloss():
    print (i.replace("-", ""))
