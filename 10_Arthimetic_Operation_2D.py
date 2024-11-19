import numpy as np

#Dealing with the 2D Array.....
var1 = np.array([[1,2,3,4],[5,6,7,8]],dtype=float)
var2 = np.array([[5,6,7,8],[1,2,3,4]],dtype=float)

print(var1)
print(var2)
print(var1+var2) #1st row of 1st Array will operate with 1st Row of 2nd Array.
print(np.add(var1,var2)) #similarly with all the operations