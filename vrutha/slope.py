# here I will apply a simple logic insted of reading values of x I will just read the m and c.
# then from the user I will read y1 and x1.
# Then I will compute ( x1*m + c ) if this value is equal to the value y1 of the user entry then.
# the point lies in a line else not
# using matpolt lib I will show the same for some auto genrated X and Y...

import numpy as np 
import matplotlib.pyplot as plt 
print("Enter the slope value..")
m = int(input())
c = int(input("Enter the Intercept.."))
x1 = int(input("Enter the X1.."))
y1 = int(input("Enter the Y1.."))
# compute ( x1*m + c ) and compare with y1
if (( x1*m + c ) == y1):
    print("The point lies on a line")
else :
    print("Not")





x = np.arange(0,10,1) 
y = m*x + c
#Labeling the Axes and Title
plt.title("Finding point is on line or not..") 
plt.xlabel("x - axis") 
plt.ylabel("y - axis") 

# Formatting the line colors
plt.plot(x,y,'r')

# Formatting the line type  
plt.scatter(x1, y1)
plt.show()