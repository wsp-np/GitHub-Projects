from pathlib import Path
import csv

fp = Path.cwd()/"cash-on-hand.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file: 
    reader = csv.reader(file)
    next(reader)

    listofaccumulatedcashonhand = []
    listofdays = []
    for row in reader:
        listofaccumulatedcashonhand.append(int(row[1]))
        listofdays.append(int(row[0]))

def cashonhand():
    day0 = listofaccumulatedcashonhand[0]
    deficit = False
    deficitdays = []
    for i in range(len(listofaccumulatedcashonhand)-1):
        difference = listofaccumulatedcashonhand[i+1] - day0
        if difference < 0:
            deficitdays.append(f"[CASH DEFICIT] DAY: {listofdays[i+1]}, AMOUNT: USD{round(difference,1)}\n")
            deficit = True
        day0 = listofaccumulatedcashonhand[i+1]
    if deficit == False:
        deficitdays.append(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY.\n")
    return deficitdays
for i in cashonhand():
    print (i.replace("-", ""))

   

   
