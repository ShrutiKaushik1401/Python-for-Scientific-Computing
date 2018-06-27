
# coding: utf-8

# In[4]:


print("Shruti Kaushik Python Project 1. \n" 
      "Please  change the directory path of the file in below Load_Text command. \n")

'''Project Objective and Data -
'Perform Resampling and Interpolation/Extrapolation of time series data'

I intend to use various Python packages like pandas, numpy, scipy and matplotlib to perform up-sampling 
and down-sampling on the time series data and plot the results for better understanding. 

Dataset - I have prepared a ‘Monthly Sales dataset for the Diabetes Control Pills over the period of 2015-2017’.

Down-sample - time series data to a ‘lower frequency’ and summarize the higher frequency observations. Here, I will 
decrease the frequency of the data samples from ‘Months to Quarters / Years’ and calculate the quarterly mean and total annual sales of the product.

Up-sample - time series data to a ‘higher frequency’ and interpolate the new observations. Here, I will increase the 
frequency of the data samples from ‘Monthly to Daily’ sales and determine how the fine-grained observations
are calculated using scipy interpolation.
'''

# 1- Import the required packages
import pandas as pd
import numpy as np
import scipy as sp
from matplotlib import pylab as plb
from scipy.interpolate import interp1d


# 2 - Load the monthly Diabetes Control Pills Sales dataset for past 3 years 
#2015-2017 from a text file to pandas dataframe
df_Sales = pd.read_table(r'C:\Users\ShrutiK\Python for Data Analysis and Scientific Computing\Shruti_Kaushik_Python_Project\Diabetes_Control_Pill_Sales_Dataset.txt'
   , delim_whitespace=True)

# 3 - Convert the Months column from string to datetime to apply sampling
df_Sales = pd.DataFrame(df_Sales)
df_Sales.Month = pd.to_datetime(df_Sales.Month)
print('\n Original dataset', df_Sales)

#QUARTERLY MEAN SALES - Down - Sampling and Plotting using matplotlib and pandas
# 4 - Resample the data decreasing the frequency of Sales to quarterly from monthly 
#and calculate mean quarterly sales
df_Sales_Downsampled_Qtr = df_Sales.resample('Q', on='Month')
print('\n With decreased freqency resampling, quarterly mean is: \n', df_Sales_Downsampled_Qtr.mean())

# 5 - Plot the Quarterly mean sales
plb.figure(figsize=(20,12), dpi=120) # dpi is dots per inch
plb.subplot(2,1,2)
#Title, labels, legends
plb.title("Quarterly Mean Sales")
plb.xlabel("Quarter")
plb.ylabel("Sales")
plb.legend(loc="upper right")
plb.plot(df_Sales_Downsampled_Qtr.sum(),color = 'red', linewidth = 1.5, linestyle = "--", 
         label = 'Quarterly Mean Sales')
plb.show()
plb.pause(1)


#YEARLY TOTAL SALES Down- Sampling and Plotting using matplotlib and pandas
# 6- Resample the data decreasing the frequency of Sales to yearly 
#for year-end frequency and use #sum to calculate the total sales each year.
df_Sales_Downsampled_Yrly = df_Sales.resample('A', on='Month')
print('\n With decreased freqency resampling,yearly total of the sales is: \n', df_Sales_Downsampled_Yrly.sum())
      
# 7 - Plot the Yearly Total sales
plb.figure(figsize=(8,6), dpi=120) # dpi is dots per inch
plb.subplot(2,1,2)
#Title, labels, legends
plb.title("Annual Total Sales")
plb.xlabel("Year")
plb.ylabel("Sales")
plb.legend(loc="upper right")
plb.plot(df_Sales_Downsampled_Yrly.sum(),color = 'blue', linewidth = 1.5, linestyle = "-.", label = 'Annual Sales')
plb.show()
plb.pause(1)


# 8- USe of NUMPY and SCIPY - Interpolate the data by increasing the frequency of Sales 
#to Daily from Monthly. 

#Create a numpy array from pandas dataframe
arr_Sales = df_Sales.values
print('\n Numpy array for existing dataset: \n',arr_Sales)
                                            
#Get the Month of numpy array and convert to datetime to plot as x axis
x = pd.to_datetime(np.array(arr_Sales[:,0]))
print('\n X-Axis - Months - : \n',x)

#Get the Sales of numpy array to plot as y axis
y = arr_Sales[:,1]
print('\n Y-Axis - Sales - : \n',y)

#Apply interpolation to fill the missing values for all the days of the January month.
f = sp.interpolate.interp1d(x, y,kind = 'slinear',fill_value='extrapolate')

#Calculate the new x axis to have all the days of the month, we pick Jan'17 to upsample on daily basis 
start = pd.Timestamp('2017-01-01')
end = pd.Timestamp('2017-01-31')
x_Daily = np.linspace(start.value, end.value,'31')
x_Daily = pd.to_datetime(x_Daily)
print('\n Days of the month: \n',x_Daily) 

#Calculate the daily Sales, new y axis , for Daily data
y_Daily = f(x_Daily) 
print('\n Interpolated Daily Sales for the month of January: \n',y_Daily)

#Plot the Daily Sales for the month of January'17
fig = plb.figure(figsize=(10,6), dpi=60)
plb.subplot(2, 1, 2)
plb.title("Daily January'17 Sales")
plb.xlabel("Days")
plb.ylabel("Sales")
plb.legend(loc="upper right")
plb.plot(x_Daily,y_Daily,color = 'green', linewidth = 1.5, linestyle = "-.", label = 'Daily Sales' )
plb.pause(1)


# 9 - USe of NUMPY and SCIPY - Extrapolate to predict the future sales for 2018
#Calculate the new x axis for the year 2018
start = pd.Timestamp('2018-01-01')
end = pd.Timestamp('2018-12-31')
x_Prediction = np.linspace(start.value, end.value,'12')
x_Prediction = pd.to_datetime(x_Prediction)
print('\n Months of 2018: \n',x_Prediction)

#Calculate the Predicted Sales for 2018, new y axis
y_Prediction = f(x_Prediction)
print('\n Predicted Sales of 2018: \n',y_Prediction)

#Plot the Predicted Monthly Sales for the 2018 w.r.t current data
fig = plb.figure(figsize=(10,6), dpi=60)
plb.subplot(2, 1, 2)
plb.title("Predicted Monthly Sales for 2018")
plb.xlabel("Months")
plb.ylabel("Sales")
plb.legend(loc="upper right")
plb.plot(x,y,'o',x_Prediction,y_Prediction,'-.')
plb.pause(1)


print('\n Shruti Kaushik Python Project 1 finishes here.\n')

