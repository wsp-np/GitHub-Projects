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
    
    # convert string to integer using int()
    for row in reader:
        listofaccumulatedcashonhand.append(int(row[1]))
        listofdays.append(int(row[0]))
 
# create a function to calculate the difference in cash on hand 
def cashonhand(): 
    """
    Function calculates the difference in cash on hand and returns cash deficit if the current day has a lower cash on hand than the previous day.
    This function does not require any parameters. 
    """
    # create a variable to store the first index of the first index in the extracted list
    first_index = listofaccumulatedcashonhand[0]
    
    # set deficit to False 
    deficit = False
    
    # create an empty list to append output data
    deficitdays = [] 
    
    # loop through the function to calculate daily cash on hand using for loop
    # use i to indicate the index position of the values in the list 
    for i in range(len(listofaccumulatedcashonhand)):
        # find the difference in cash on hand between the current and previous day
        difference = listofaccumulatedcashonhand[i] - first_index
        # check if there is a difference in cash on hand 
        if difference < 0: 
            # evaluate and state that there is cash deficit when the difference in cash on hand calculated is negative
            deficitdays.append(f"[CASH DEFICIT] DAY: {listofdays[i]}, AMOUNT USD{round(difference,1)})")
            # set deficit to True for loop to stop looping 
            deficit = True
        # update the previous day variable after looping
        first_index = listofaccumulatedcashonhand[i]
                               
    # evaluate if there is no deficit
    if deficit == False:
        # evaluate and state that there is cash surplus when there is no decrease in cash on hand throughout
        deficitdays.append(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY.")                     
    # return the days that has cash deficit 
    return deficitdays 
                               
# print the days with cash deficit in the cashonhand list using print()
for i in cashonhand(): 
    # replace the - in cash deficit amount by replacing it with a blank
    print(i.replace("-",""))
