
# coding: utf-8

# In[109]:


#1  - Include a section with your name
print("Shruti Kaushik HW2: \n")

#Assignment Begins
import numpy as np
from numpy import matrix, array, int32, random, str


#2 -  Create matrix A with size(3,5) containing random numbers 
A = np.random.random(15) # Create 15 random numbers 
A = np.reshape(A,(3,5)) # reshape it to 3,5 
A = matrix(A) # convert to matrix
print("Answer 2 - Matrix A of size 3,5 is as below : \n", A)


#3 - Find the size and length of matrix A
print('\n Answer 3 - Length of A is :', len(A)) # Answer - 3
print('\n Answer 3 - Size of A is :', A.size) # Answer - 15


#4 -  Resize (crop/slice) matrix A to size (3,4)
#Assumption - As the original matrix has been resized, 
#hereafter all the operations on and using this matrix A will be done on new size 3,4
#If this is not desired, we need to create a copy of original matrix A and resize the copy to 3,4 
#so the original shape of A is retained.
A = A[:,:4]
print("\n Answer 4 - Resized Matrix A of size 3,4 is as below : \n", A)


#5 - Find the transpose of matrix A and assign it to B with above assumption
B = A.T
print("\n Answer 5 - Transpose of A - Matrix B is as below : \n", B)


#6 - Find the minimum value in column 1 of matrix B. 
#Understanding, find minimum value in the first column of B which will be represented as B[:,0]
print('\n Answer 6 - Minimum value in column 1 of B is : ' , B[:,0].min())

#7 - Find the minimum and maximum values for the entire matrix A
print('\n Answer 7 - Minimum value of matrix A is : ', A.min())
print('\n Answer 7 - Maximum value of matrix A is : ', A.max())


#8 - Create vector X (an array) with 4 random numbers
X = np.random.random(4)
print("\n Answer 8 - Vector X is as below : \n", X)


#9 - Create a function and pass vector X and matrix A in it
#10  - In the new function multiply vector X with matrix A and assign the result to D

def matrix_mult(vector,matrix):
    D = np.dot(matrix,vector)
    return D
#Caller    
D = matrix_mult(X,A)
print('\n Answer 9 & 10 - The matrix multiplication of X and A i.e. D is : ' , D)


#11 - Create a complex number Z with absolute and real parts !=0
Z = complex(5,4)
print('\n Answer 11 - Complex number Z is : ', Z) # (5+4j)


#12 - Show its real and imaginary parts as well as it’s absolute value
print('\n Answer 12 - Real part of Z is :', Z.real) # real part 5.0
print('\n Answer 12 - Imaginary part of Z is :',Z.imag) # imaginary part 4.0
print('\n Answer 12 - Absolute value of Z is :',abs(Z)) # absolute value 6.4031242374328485

#13 -  Multiply result D with the absolute value of Z and record it to C
C = D * abs(Z)
print('\n Answer 13 - Product of D and Z i.e. C is : ', C)

#14 - Convert matrix B from a matrix to a string and overwrite B
# Disclaimer - Matrix B has decimal numbers and converting them to string will result in multiple decimal
# points in the string. If that is expected, below is the solution. Else we can str(int(round(item)))
# and then only create a string of whole numbers.

itemString = '' # create an empty string
for item in np.nditer(B): # iterate through all the elements of the matrix B
    itemString += str(item) # convert the elements to string
#print(itemString)
B = itemString
print('\n Answer 14 - New value of B after matrix to string conversion is : ', B)


#15 -  Display a text on the screen: ‘Your Name is done with HW2'
print ("\n Shruti Kaushik is done with HW2. \n")

