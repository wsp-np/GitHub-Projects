from pathlib import Path
import matplotlib.pyplot as plt # ensure you have intalled matplotlib before importing it. available in the project brief.
import csv

#--------------- PART 1: This part of the program is completed for you --------------#

# create a file to csv file.
fp = Path.cwd()/"superstore_transaction.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create 3 empty lists to store profit and quantity by each cluster
    cluster1 = [] 
    cluster2 = []
    cluster3 = []

    # append profit and quantity as a list back to each empty list
    for row in reader:
                
        if row[4] == "Cluster 1":
            cluster1.append([row[13], row[14]])
        elif row[4] == "Cluster 2":
            cluster2.append([row[13], row[14]])
        else:
            cluster3.append([row[13], row[14]])
        
#---------------------------- PART 2: Insert your own code ---------------------------#
# 1. Calculate the total profit and total quantity using cluster 1,2,3 variables from part 1
# 2. Write the calculated profit to a txt file. Name it as cluster_report.txt.

#create a function to calculate the total profit of all 3 clusters
def profit_calculator(): 
    """ 
    this function calculates the total profit from the values in all 3 clusters.
    """

    # create an empty list to store profit for cluster 1
    pro1 = []
    # use for loop to extract profit from cluster 1
    for cp1 in cluster1:
            # use [0] to index and extract profit
            # use .replace to remove $ sign and comma
            p1 = cp1[0].replace("$", "")
            p1 = p1.replace(",","")
            # use float() to convert string to float
            pro1.append(float(p1))
            
    # create an empty list to store profit for cluster 2
    pro2 = []
    # use for loop to extract profit from cluster 2
    for cp2 in cluster2:
            # use [0] to index and extract profit
            # use .replace to remove $ and comma
            p2 = cp2[0].replace("$", "")
            p2 = p2.replace(",","")
            #use float() to convert string to float
            pro2.append(float(p2))

    # create an empty list to store profit for cluster 3
    pro3 = []
    # use for loop to extract profit from cluster 3
    for cp3 in cluster3:
            # use [0] to index profit to extract
            # use .replace to remove $ and comma
            p3 = cp3[0].replace("$", "")
            p3 = p3.replace(",","")
            # use float() to convert string to float
            pro3.append(float(p3))

    # send values of total profit from all 3 clusters back to the program using f-string
    # use \n to create a new line and use sum() to sum all the values in each cluster
    return f"\n Cluster 1: ${sum(pro1)} \n Cluster 2: ${sum(pro2)} \n Cluster 3: ${sum(pro3)}"

# create a function quantity_calculator to calculate the total quantity of all 3 clusters
def quantity_calculator():
    """
    This function calculates the total quantity for each clusters.
    """
    
    # create an empty list to store quantity for cluster 1 
    qt1 = []
    # use for loop to extract quantity for cluster 1
    for qnt in cluster1:
        # convert the string to float using float()
        # use [1] to index quantity data to be extracted
        qt1.append(float(qnt[1]))

    # create an empty list to store quantity for cluster 2
    qt2 = []
    # use for loop to extract quantity data from cluster 2
    for qnt2 in cluster2:
        # use float() to convert string to float
        # use [1] to index quantity data to be extracted
        qt2.append(float(qnt2[1]))

    # create an empty list to store quantity for cluster 3
    qt3 = []
    # use for loop to extract quantity data from cluster 3
    for qnt3 in cluster3:
        # use float() to convert string to float
        # use [1] to index quantity data to be extracted 
        qt3.append(float(qnt3[1]))

    # send values of total quantity of all 3 clusters back to the program using f-string
    # use \n to create new line and sum() to add values in each cluster together
    return f"\n Cluster 1: {sum(qt1)} \n Cluster 2: {sum(qt2)} \n Cluster 3: {sum(qt3)}"

from pathlib import Path
# create a file to text file 
fp = Path.cwd()/"cluster_report.txt"

# use "w" to write calculations of total profit and quantity of all 3 clusters into the text file.
with fp.open(mode= "w", encoding= "UTF-8") as file:
    # use file.write to write information
    # use \n to create a new line
    file.write("PROFIT REPORT \n")
    # use = * 13 to create the divider line
    file.write("="*13)
    # use profit_calculator() to insert function 
    file.write(profit_calculator())
    # use \n * 2 to create 2 new line
    file.write("\n"*2)
    file.write("QUANTITY REPORT \n")
    # use = * 15 to create the divider line
    file.write("="*15)
    # use quantity_calculator() to insert function
    file.write(quantity_calculator())

#--------------- PART 3: This part of the program is completed for you  --------------#

# This part of the program plots the profits and quantities by clusters.
# The values profits and quantities are hard-coded, so it is not link to part 2. 
# Even if part 2 does not work, part 3 can still be executed.
# Simply execute the code and the plot will be saved as an image file.
# Click on the png file in the explorer panel to see the barplot.

# Do not worry about how the code below works.
# It is an example of visualising data using Python. 
# You will learn about data visulisation in analytics module in year 2. 

cluster_profit = [133426, 43684, 109224] # hardcoded profit by clusters 
cluster_quantity = [18632, 8716, 10524] # hardcoded quantity sold by clusters. 
fig, axs = plt.subplots(2, figsize = (10,7))
fig.suptitle("SuperStore Business Performance")
cluster = ["cluster 1", "cluster 2", "cluster 3"]
axs[0].bar(cluster, cluster_profit)
axs[1].bar(cluster, cluster_quantity)
axs[0].set_xlabel("Profit by Clusters")
axs[1].set_xlabel("Quantity Sold by Clusters")
axs[0].set_ylabel("Profit ($)")
axs[1].set_ylabel("Quantity (000s)")
fig.savefig("cluster_barplot.png") 
plt.imread("cluster_barplot.png")
plt.show()












