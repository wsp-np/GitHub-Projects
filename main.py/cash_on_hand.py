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
 
# create a function to calculate the difference for cash on hands 
def cashonhand(): 
    """
    Function calculates the difference in cash on hand and returns cash deficit if the current day has a lower cash on hand than the previous day.
    This function does not require any parameters. 
    """
    # create a variable to store the index of the first value in the extracted list
    day0 =listofaccumulatedcashonhand[0] 
    # set deficit to false 
    deficit = False 
    # create empty list to append output datas
    deficitdays = [] 
    # loop through the function to calculate daily cash on hand
    # use i to indicate the index position of the values in the list 
    for i in range(len(listofaccumulatedcashonhand)-1): 
        difference = listofaccumulatedcashonhand[i+1] - day0 
        # check if there is a difference in cash on hand 
        if difference < 0: 
            # evaluate if there is deficits
            deficitdays.append(f"[CASH DEFICIT] DAY: {listofdays[i+1]}, AMOUNT USD{round(difference,1)})" 
            # set deficit to true for loop to stop looping 
            deficit = True 
        day0 = listofaccumulatedcashonhand[i+1]
    # evaluate if there is no deficits
    if deficit == False: 
        deficitdays.append(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY.")
    # return the days that has cash deficit 
    return deficitdays 
# print the days with cash deficit in the cash on hand list
for i in cashonhand(): 
    # print the function and replace the negative sign in cash deficit amount by replacing it with a blank to execute it
    print(i.replace("-","") 
