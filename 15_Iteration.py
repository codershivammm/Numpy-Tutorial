import numpy as np

#ITERATING IN 1-D ARRAYS

var1 = np.array([1,2,3,4,5])
print(var1)
print("Iterating")
for i in var1 :
    print(i)

#ITERATING IN 2-D ARRAYS

var2 = np.array([[1,2,3,4],[5,6,7,8]]) 
print(var2)
print("Iterating")
for i in var2:
    for j in i:
        print(j)
    
#ITERATING IN 3-D ARRAYS

var3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(var3)
print("Iterating")
for i in var3:
    for j in i:
        for k in j:
            print(k)

#ITERATING USING np.nditer() 

var3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(var3)
print("Iterating")
for i in np.nditer(var3):
    print(i)

#ITERATING AND INDEXING BOTH WITH np.ndnumerate()

var3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(var3)
print("Iterating")
for i,d in np.ndenumerate(var3):
    print(i,d)
