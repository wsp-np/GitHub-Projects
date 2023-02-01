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
    
    # convert string to integer using int()
    for row in reader:
        listofaccumulatedprofits.append(int(row[4]))
        listofdays.append(int(row[0]))

# create a function to calculate the difference in profit 
def profitandloss():
    """
    Function calculates the difference in net profits and returns profit deficit if the current day has a lower profit than the previous day.
    This function does not require any parameters.
    """
    # create a variable to store the index of the first value in the extracted list
    day0 = listofaccumulatedprofits[0]
    
    # set deficit to False
    deficit = False
    
    # create an empty list to append output datas
    deficitdays = []
    
    # use for loop to calculate daily profits
    # use i to indicate the index position of the values in the list
    for i in range(len(listofaccumulatedprofits)-1):
        difference = listofaccumulatedprofits[i+1] - day0
        # evaluate if there is a difference in profits
        if difference < 0:
            # evaluate if there is deficit 
            deficitdays.append(f"[PROFIT DEFICIT] DAY: {listofdays[i+1]}, AMOUNT: USD{round(difference,1)}")
            # set deficit to True for loop to stop looping
            deficit = True
        day0 = listofaccumulatedprofits[i+1]
        
    # evaluate if there is no deficit
    if deficit == False:
        deficitdays.append(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY.")
    # return the days that has profit deficit
    return deficitdays

# execute the function using print() to print the days with profit deficit in the profitandloss list
for i in profitandloss():
    # replace the - in profit deficit amount by replacing it with a blank
    print (i.replace("-", ""))
    
