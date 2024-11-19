import numpy as np

var1 = np.matrix([[1,2],[3,4]])
var2 = np.matrix([[5,6],[7,8]])

print(var1+var2)       #Matrix Addition
print()
print(var1+var2)       #Matrix Subtraction
print()
print(var1*var2)       #Matrix Multiplication
print()
print(var1.dot(var2))  #Matrix Multiplication
print()

#Matrix Functions

#Transpose Function
var3 = np.matrix([[1,2,3],[4,5,6]])
print(var3)
print()
print(np.transpose(var3))
print()
print(var3.T)
print()

#Inverse Function
var4 = np.matrix([[1,2],[3,4]])
print(var4)
print()
print(np.linalg.inv(var4))

#Power Function
var5 = np.matrix([[1,2],[3,4]])
print(var5)
print()
print(np.linalg.matrix_power(var5,2))
print()
print(np.linalg.matrix_power(var5,0))  #will give an identity matrix
print()
print(np.linalg.matrix_power(var5,-2))

#Determinant Function
var6 = np.matrix([[1,2,3],[3,4,5],[1,2,3]])
print(var6)
print()
print(np.linalg.det(var6)) #as the two row is same in var6 matrix we get determinant as 0



#----------------------------THE END----------------------------