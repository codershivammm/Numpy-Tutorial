import numpy as np

#INDEXING IN 1-D ARRAY

var1 = np.array([1,2,3])
print(var1)
index1 = np.where(var1==2)
print("The Index of 2 is:-" ,index1)
print("Value at 1 index is :-",var1[1]) #index 1 ka value print hoga
print()

#INDEXING IN 2-D ARRAY

var2 = np.array([[1,2,3],[4,5,6]]) 
print(var2)
index2 = np.where(var2==6)
print("The Index of 6 is:-" ,index2)     
print("Value at 1,2 Index is :-",var2[1,2]) #1,2 Index ka Value print Hoga
print()

#INDEXING IN 3-D ARRAY

var3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
#finding index of 5 using np.where() function
index3 = np.where(var3==5)
print("The Index of 5 is:-" ,index3)
print("Value at Index 0,1,1,is :-",var3[0,1,1])