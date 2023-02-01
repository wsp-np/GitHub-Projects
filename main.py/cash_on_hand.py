from pathlib import Path
import csv 

# create a file to csv file  
fp= Path.cwd()/"csv_reports"/"cash-on-hand.csv"

# read the csv file to append cash on hand from the csv file 
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    
    # append accumulated cash on hand and days as a list back to each empty list 
    listofaccumulatedcashonhand =[]
    listofdays = []
    for row in header:
        listofaccumulatedcashonhand.append(int(row[1]))
        listofdays.append(int(row[0]))
 
# create a function to calculate 
def cashonhand(): 
    """
    Calculate the difference in cash on hand. This function does not require any parameters. 
    """
    day0 =listofaccumulatedcashonhand[0] # create a variable to check for the list of accumulated cash on hand 
    deficit = False 
    deficitdays = [] 
    for i in range(len(listofaccumulatedcashonhand)-1): # loop through length of accumulated cash on hand to determine if there is a differenc in profit deficit
        difference = listofaccumulatedcashonhand[i+1] - day0 
        if difference < 0: # check if there is a difference in the profit deficit 
            deficitdays.append(f"[CASH DEFICIT] DAY: {listofdays[i+1]}, AMOUNT USD{round(difference,1)}\n"
            deficit = True 
        day0 = listofaccumulatedcashonhand[i+1]
    if deficit == False: # 
        deficitdays.append(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY. \n")
    return deficitdays # return the number of deficit days 
for i in cashonhand(): 
    print(i.replace("-","") # print the function, replace the negative sign and execute the file 
