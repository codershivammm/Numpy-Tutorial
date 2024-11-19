import numpy as np

#Broadcasting allows arrays of different shapes to be combined for arithmetic operations without explicitly replicating or reshaping the arrays

var1 = np.array([1,2,3]) 
var2 = np.array([[1],[2],[3]])

print(var1)
print("Shape:-",var1.shape)
print()
print(var2)
print("Shape:-",var2.shape)
print()
var3= np.add(var1,var2)
print(var3)
print("Shape:-",var3.shape)