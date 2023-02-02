from pathlib import Path
import csv 

# create a file to csv file
fp = Path.cwd()/"csv_reports"/"profit-and-loss.csv"

# read the csv file to append profit and loss from the csv file
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    # append accumulated profit and days as a list back to each empty list
    listofaccumulated_profits = []
    list_of_days = []
    
    # convert string to integer using int()
    for row in reader:
        listofaccumulated_profits.append(int(row[4]))
        list_of_days.append(int(row[0]))

# create a function to calculate the difference in profit 
def profitandloss():
    """
    Function calculates the difference in net profits and returns profit deficit if the current day has a lower profit than the previous day.
    This function does not require any parameters.
    """
    # create a variable to store the first index in the extracted list
    first_index = listofaccumulated_profits[0]
    
    # set deficit to False
    deficit = False
    
    # create an empty list to append output data
    deficit_days = []
    
    # use for loop to loop through and calculate the daily profits
    # use i to indicate the index position of the values in the list
    for i in range(len(listofaccumulated_profits)):
        # find the difference in profits between the current and previous day
        difference = listofaccumulated_profits[i] - first_index  
        
        # evaluate if there is a difference in profits
        if difference < 0:
            # state that there is profit deficit when the difference in profits calculated is negative
            deficit_days.append(f"[PROFIT DEFICIT] DAY: {list_of_days[i]}, AMOUNT: USD {round(abs(difference),1)}")
            # set deficit to True for loop to stop looping
            deficit = True
        # update the previous day variable after looping
        first_index = listofaccumulated_profits[i]
        
    # evaluate if there is no deficit
    if deficit == False:
        # state that there is profit surplus when there is no decrease in profits throughout
        deficit_days.append(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY.")
    # return the days that has profit deficit
    return deficit_days

# execute the function using print() to print the days with profit deficit in the profitandloss list
for i in profitandloss():
    print (i)
    
