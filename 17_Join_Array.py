import numpy as np

# 1D Array
var1 = np.array([1,2,3,4,5])
var2 = np.array([6,7,8,9,0])

#print(np.concatenate((var1,var2)))

#2D Array
var3 = np.array([[1,2],[3,4]])
var4 = np.array([[5,6],[7,8]])
print(np.concatenate((var3,var4),axis=1)) #axis = 0 is along column , axis = 1 is along row

#Join array using stack() function
var5 = np.array([[1,2],[3,4]])
var6 = np.array([[5,6],[7,8]])
print(np.hstack((var3,var4))) #hstack = along row
print() 
print(np.vstack((var3,var4))) #vstack = along column
print() 
print(np.dstack((var3,var4))) #dstack = along height
print() 


#SPLIT ARRAY 

var7 =  np.array([1,2,3,4,5,6])
x = np.array_split(var3,3)
print(x)
print(x[1])


