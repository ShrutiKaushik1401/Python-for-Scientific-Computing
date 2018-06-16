
# coding: utf-8

# In[115]:


#print("Shruti Kaushik Class Exercise Lecture 5")

#Part 1 Create your data:

#2 - Work only with these imports:
import numpy as np
from numpy import matrix, array, min,max,random
from matplotlib import pylab as plb, pyplot as plt
#from math import pi

#3 - create a list A with 600 random numbers bound between (0:10)
#A = random.randint(0,10,600) # my solution will only generate integer numbers 
#but we will need to make it float later for avg.

A = list(random.random(600)*10) #AIlieve solution
#print(A)


#4 - create an array B with 500 elements bound in the range(-3*pi : 2*pi)
#B = np.random.uniform(-3*plb.pi,2*plb.pi,500) # my solution
B = plb.linspace(-plb.pi*3,plb.pi*2,500) #AIlieve solution
#print(B)


#5 - using if/for/while loop, create a function that ovwerwites every element in A that falls 
#outside of the interval[2:9] and overwrite that element with the average between 
#the smallest and largest element in A
def overwrite_A(A):
    #A = A.astype(float) # convert A to float as the average is a float number
    #print(A)
    a_avg = (min(A) + max(A))/2 #4.5
    
    for index, item in enumerate(A): #loop thrugh all items index wise
        if item < 2 or item >= 9:  #check for item outside of range [2:9] includes 2 and 9                  
            item = a_avg
            A[index] = item # replace item with average value
            #A[index] = A[index] * 0.1 #6 - Ailiev slution - Normalize each list element to be bound between[0:0.1]
            
    #6 - Normalize each list element to be bound between[0:0.1]
    A = (0.1*(A - np.min(A))/np.ptp(A)) # my solution
    
    return A
        
# 7 - Return the result from the function to C
C = overwrite_A(A)

#8 - Cast C as an array
C = array(C)
#print(C)

#9 - Add C to B (think of C as noise) and record the result in D
D = B + C[:len(B),] # capture 500 elements from C to match to size of B
#print(D)

#SORT IT prior to plotting
#Part	2	-	plotting:
#10 -  Create	a	ﬁgure,	give	it	a	title	and	specify	your	own	size	and	dpi	
plb.figure('Plotting signals' , figsize=(6,4), dpi=100)


#11 - Plot	the	sin	of	D,	in	the	(2,1,1)	location	of	the	ﬁgure
#12 - Overlay	a	plot	of	cos	using	D,	with	diﬀerent	color,	thickness	and	type	of	line
plb.subplot(2,1,1)
d_sin = plb.sin(D)
d_cos = plb.cos(D)
plb.title("Function of Sin and Cos")
plb.plot(D,d_sin, color = "b", linewidth=1.5, linestyle="--", label = 'sin')
plb.plot(D,d_cos, color = "r", linewidth=1, linestyle="-.", label = 'cos')


#13. Create	some	space	on	top	and	bottom	of	the	plot	(on	the	y	axis)	and	show	the	grid
plb.ylim(-1.12,1.12)
plb.grid()

#14 - Specify	the	following:	title,	Y-axis	label	and	legend	to	ﬁt	in	the	best	way
plb.ylabel('Y-axis')
plb.title('Signals')
plb.legend(loc='best')


#15. Plot	the	tan	of	D,	in	location	(2,1,2)	with	grid	showing,	X-axis	label,	Y-axis	label	and
#legend	on	top	right	
plb.subplot(2,1,2)
d_tan = plb.tan(D)
plb.plot(D,d_tan, label='tan')
plb.grid()
plb.xlabel('X-axis')
plb.ylabel('Y-axis')
plb.legend(loc="upper right")

print("Shruti Kaushik is done with Classroom Assignment for lecture 5")

