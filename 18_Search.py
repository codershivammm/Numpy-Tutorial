import numpy as np

#SEARCHING THE VALUE AND GETTING INDEX OF CORRESPONDING VALUE

var = np.array([1,5,4,6,8,2,3,8,2,6,4,9,2,4,8,9,2])
print(np.where(var==2))  #gives all indexes of 2 in the array

#SEARCHSORTED FUCTION

var1 = np.array([1,5,4,6,8,2,3,8,2,6,4,9,2,4,8,9,2])
print(np.searchsorted(var1,8)) #It will first sort the array then tell the index where the 8 fits best to be inserted 

#INSERT FUCTION
#np.insert(array, index, values, axis=)

var = np.array([1,5,4,6,8,2,3,8,2,6,4,9,2,4,8,9,2])
print(np.insert(var1,14,8,axis=None))


