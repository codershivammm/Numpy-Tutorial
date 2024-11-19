import numpy as np

#Dealing with 1-D Array
var1 = np.array([1,2,3,4] ,dtype=float)
var2 = np.array([5,6,7,8],dtype=float)

varadd = var1 + 3 #simillarly can be done with "-" or "*" or  "/" or "%"
print(varadd)
print(var1+var2)  #simillarly can be done with "-" or "*" or  "/" or "%"
print(np.add(var1,var2)) 
print(np.subtract(var1,var2)) 
print(np.multiply(var1,var2)) 
print(np.divide(var1,var2)) 
print(np.mod(var1,var2)) 
print(np.power(var1,var2)) #Raises each element in var1 to the power of the corresponding element in var2.
print(np.reciprocal(var1)) 