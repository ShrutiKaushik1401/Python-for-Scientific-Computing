
# coding: utf-8

# In[150]:


# Midterm Test

# import the required libraries
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pylab as plb
import math
import datetime


#create an array A with 12 elements beginning from number 5, containing consecutive odd numbers
A = np.arange(5,29,2)
print('Original Aray A is:' ,A)

#compute the simple moving average of an array(SMA),using an adjustable window using a function. 
#the function calculating the SMA of the array must take 2 input argumants 
#1. the array(A)
#2. a window width with a default vaue = 2

def compute_SMA(A,N):
    step = N
    SMA = np.zeros(len(A)-1).astype(int) #initialize an array SMA  with zeros
     
    for i, x in enumerate(A): # loop through each element of A
        if i < len(A)-1: #Loop till last element of A
            Simple_Avg = (A[i] + A[i+1])/step # Calculate simple moving average
            SMA[i] = Simple_Avg # append the SMA to Array SMA
    return SMA

#Make 2 function calls to the SMA:
#1st call - pass array A only. Save this SMA to B
B = compute_SMA(A,2)
print('Simple Moving Average Array B is:',B)

#2nd call specifying a window width = 4, save this SMA to C
C = compute_SMA(A,4)
print('Simple moving Average C with window 4 is:',C)

#After every SMA is collected(As array) calculate its cumulative moving average(CMA)
def compute_CMA(SMA):
    CMA = np.zeros(len(SMA)-1).astype(float) #initialize an array CMA  with zeros    
    N=2
    Sum = SMA[0]
        
    for i, x in enumerate(SMA):
        if i < len(SMA)-2:
            Sum = Sum + SMA[i+1] 
            CMA[i] = Sum/(i+N)        
    return CMA

Z = compute_CMA(B)
print('Cumulative moving average array Z is:',Z)

# 