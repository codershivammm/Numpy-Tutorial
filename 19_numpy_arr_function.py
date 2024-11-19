import numpy as np

#SHUFFLE
var = np.array([1,2,3,4,5])
np.random.shuffle(var)
print(var)

#UNIQUE
var1 = np.array([1,2,3,2,4,3,2,5])
print(np.unique(var1,return_index=True,return_counts=True)) #return counts give no of times the number got repeated

#FLATTEN --------> Used to covert 2-D Array to 1-D Array
var2 = np.array([1,2,3,4,5,6]) #1d array
x = np.resize(var2,(2,3))
print(x)
print(x.ndim) #2d array hogya

y = x.flatten()
print(y)
print(y.ndim) #1D array me covert hogya


