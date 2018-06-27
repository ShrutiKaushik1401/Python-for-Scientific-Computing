
# coding: utf-8

# In[3]:


print("Shruti Kaushik Python Project 2. \n" 
      "Please  change the directory path of the file in below Load_Text command. \n")

'''Project Objective and Data - To perform data analysis on the Store Sales data and 
understand the customer's purchase patterns such as - 
•How many customers have purchased an item of particular category?
•Which customers have purchased items of all categories?
•How many customers have purchased items of only few categories? etc.'''

# 1- Import the required libraries
import pandas as pd
import numpy as np
from matplotlib import pylab as plb


# 2 - Load the Sales dataset from a text file to pandas dataframe
df_Store_Sales = pd.read_table(r'C:\Users\ShrutiK\Python for Data Analysis and Scientific Computing\Shruti_Kaushik_Python_Project\Sales Dataset.txt'
   , delimiter=',', usecols=[0,1,3,4,5,7])

df_Store_Sales = pd.DataFrame(df_Store_Sales)

#Create a numpy array for the sales dataset
arr_Store_Sales = df_Store_Sales.values
print(arr_Store_Sales)
                                            
#Get the aggregated Sale Price for the orders for each category
x = df_Store_Sales.groupby('Category')['Unit_Price'].sum()
print(x)

#Get the unique category of sales
y = np.unique(arr_Store_Sales[:,2])
print(y)

#Plot the sales for each category
fig = plb.figure(figsize=(10,6), dpi=120)
plb.figure("Categorical Sales")
plb.axes([0.035,0.035,0.9,0.9])
colormap = plb.cm.Dark2.colors 
plb.cla()
plb.pie(x,labels=y,colors=colormap,radius=.75,autopct='%1.2f%%', shadow=True,startangle=15)
#we set the aspect ratio to 'equal' so the pie is drawn in circle
plb.axis('equal')
plb.xticks(())
plb.yticks(())
plb.show()
plb.pause(1)
print('\n From the pie chart, we can conclude that majority of the customers buy Hat from the store \n ')

#Create the sets for each category and Initialize them to empty values:
Beer = set()
Sunscreen = set()
Hat = set()

#Read each line of the file, get the customer information and add to the appropriate set. 
for row in arr_Store_Sales:
        customer = (row[0],row[1])
        category = row[2]
        if category == "Beer":
                Beer.add(customer)
        if category == "Sunscreen":
                Sunscreen.add(customer)
        if category == "Hat":
                Hat.add(customer)
                
#Print the customers for each category                
print('\n Customers purchasing Beer are: \n', Beer)
print('\n Customers purchasing Sunscreen are: \n',Sunscreen)
print('\n Customers purchasing Hat are: \n',Hat)

#Performing Data analysis 
print("%s customers have purchased Beer" % len(Beer))
print("%s customers have purchased Sunscreen" % len(Sunscreen))
print("%s customers have purchased Hat" % len(Hat))
print("%s customers have purchased Hat and Sunscreen" % len(Hat & Sunscreen))
print("%s customers have purchased Beer and Sunscreen" % len(Beer & Sunscreen))
print("%s customers have purchased Beer, Sunscreen and Hat" % len(Beer & Sunscreen & Hat))
print("\n The following customers are our most valued customers as they have purchased all the 3 items: \n")
for customer in Beer & Sunscreen & Hat:
        print(customer)

print("\n Shruti Kaushik Python Project 2 finishes here.\n")

