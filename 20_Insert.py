import numpy as np

var1 = np.array([1,2,3,4,5])

#np.insert(arrayname, index, values, axis=)
#np.delete(arrayname , index)

print(np.insert(var1,(2,3), 10))  #Inserts 10 at 2nd and 3rd Index
print(np.append(var1,9))          #Inserts or append 9 at the end of the array
print(np.delete(var1,3))          #deletes the value at index 3
